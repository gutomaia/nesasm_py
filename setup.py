import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'VERSION.txt')) as f:
    VERSION = f.read().strip()

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIREMENTS = [line for line in iter(f)]

setup(
    name='nesasm',
    version=VERSION,
    description='NES Assembly Compiler',
    author='Gustavo Maia Neto (Guto Maia)',
    author_email='guto@guto.net',
    license='GPL3',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'examples']),
    scripts=['bin/nesasm'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Assembly',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Embedded Systems',
    ],
    url='http://github.com/gutomaia/nesasm_py/',
    install_requires=REQUIREMENTS,
)
