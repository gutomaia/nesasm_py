from setuptools import setup, find_packages
import os

setup(name = 'pyNES',
      version = '0.1',
      description = 'A NES ASM Compiler and SDK',
      #long_description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
      author = "Gustavo Maia Neto (Guto Maia)",
      author_email = "guto@guto.net",
      license = "GPL3",
      packages = find_packages(),
      #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Programming Language :: Assembly',
          'Topic :: Games/Entertainment',
          'Topic :: Software Development :: Assemblers',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Compilers',
          'Topic :: Software Development :: Embedded Systems',
        ],
      url = 'http://github.com/gutomaia/pyNES/',
)
