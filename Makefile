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
	@rm python.mk
	@rm github.mk
	@rm tools

build: python_build

install:
	${VIRTUALENV} python setup.py develop

test: python_build ${REQUIREMENTS_TEST} install
	${VIRTUALENV} nosetests --processes=2 -e image_test.py

${NESASM_C_MAKE}:
	mkdir -p tools
	cd tools && git clone https://github.com/toastynerd/nesasm.git

${NESASM_C_BIN}: ${NESASM_C_MAKE}
	@$(MAKE) -C ${NESASM_C_PATH}

tools: ${NESASM_C_BIN}

ci: install tools
	${VIRTUALENV} CI=1 nosetests

pep8: ${REQUIREMENTS_TEST}
	${VIRTUALENV} pep8 --statistics -qq pynes | sort -rn || echo ''

todo:
	${VIRTUALENV} pep8 --first pynes
	find pynes -type f | xargs -I [] grep -H TODO []

search:
	find pynes -regex .*\.py$ | xargs -I [] egrep -H -n 'print|ipdb' [] || echo ''

report:
	coverage run --source=pynes setup.py test

tdd:
	${VIRTUALENV} tdaemon --ignore-dirs="build,dist,bin,site,pynes.egg-info,venv,.tox" --custom-args="-e image_test.py --with-notify --no-start-message"

tox: ${REQUIREMENTS_TEST}
	${VIRTUALENV} tox

dist: python_egg python_wheel

register:
	${VIRTUALENV} python setup.py register -r pypi

distribute: dist
	${VIRTUALENV} python setup.py bdist_egg bdist_wheel upload -r pypi

.PHONY: clean linux windows dist nsis installer run report ghpages
