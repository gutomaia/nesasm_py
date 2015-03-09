# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from distutils.core import Command
from unittest import TextTestRunner, TestLoader

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIREMENTS = f.read()


class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = TestLoader()
        suite = loader.discover('nesasm/tests', pattern='*_test.py')
        TextTestRunner(verbosity=4).run(suite)


setup(
    name='nesasm',
    version='0.0.3',
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
    cmdclass={'test': TestCommand},
    test_suite='nesasm.tests',
    install_requires=REQUIREMENTS,
)
