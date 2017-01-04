PLATFORM = $(shell uname)

PROJECT_NAME=NESasm
PROJECT_TAG?=nesasm

PYTHON_MODULES=nesasm

NESASM_C_PATH=tools/nesasm
NESASM_C_MAKE=${NESASM_C_PATH}/Makefile
NESASM_C_BIN=${NESASM_C_PATH}/bin/nesasm

WGET = wget -q

OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}" ; fi

default: python.mk github.mk
	@$(MAKE) -C . test

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

ifeq "true" "${shell test -f github.mk && echo true}"
include github.mk
endif

python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && \
		touch $@

github.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/github.mk && \
		touch $@

clean: python_clean

purge: python_purge
	@rm -rf python.mk github.mk
	@rm -rf tools
	@rm -rf .tox

build: python_build

test: python_build ${REQUIREMENTS_TEST} ${CHECKPOINT_DIR}/.python_develop
	${VIRTUALENV} nosetests --processes=2

${NESASM_C_MAKE}:
	mkdir -p tools
	cd tools && git clone https://github.com/toastynerd/nesasm.git

${NESASM_C_BIN}: ${NESASM_C_MAKE}
	@$(MAKE) -C ${NESASM_C_PATH}

tools: ${NESASM_C_BIN}

ci: build ${REQUIREMENTS_TEST} ${CHECKPOINT_DIR}/.python_develop tools
	${VIRTUALENV} CI=1 nosetests -v --with-timer --timer-top-n 0

pep8: ${REQUIREMENTS_TEST}
	${VIRTUALENV} pep8 --statistics -qq nesasm | sort -rn || echo ''

todo:
	${VIRTUALENV} pep8 --first nesasm
	find nesasm -type f | xargs -I [] grep -H TODO []

search:
	find nesasm -regex .*\.py$ | xargs -I [] egrep -H -n 'print|ipdb' [] || echo ''

report:
	${VIRTUALENV} coverage run --source=nesasm setup.py test

tdd:
	${VIRTUALENV} tdaemon --ignore-dirs="build,dist,bin,site,nesasm.egg-info,venv,.tox" --custom-args="-e image_test.py --with-notify --no-start-message"

tox: ${REQUIREMENTS_TEST}
	${VIRTUALENV} tox

dist: python_egg python_wheel

register:
	${VIRTUALENV} python setup.py register -r pypi

distribute: dist
	${VIRTUALENV} python setup.py bdist_egg bdist_wheel upload -r pypi

.PHONY: install clean report dist register distribute ghpages
