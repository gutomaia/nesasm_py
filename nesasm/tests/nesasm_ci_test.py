from nesasm.tests import HexFileTestCase
from unittest import SkipTest
from os import remove
from os.path import abspath, basename, dirname, exists, splitext
from glob import glob

NESASM_C_BIN = abspath('tools/nesasm/bin/nesasm')
NESASM_PY_BIN = abspath('bin/nesasm')

def nesasm_c(_input):
    from subprocess import Popen
    path = dirname(_input)
    p = Popen([NESASM_C_BIN, _input], cwd=path)
    p.wait()

def nesasm_py(_input):
    from subprocess import Popen
    path = dirname(_input)
    p = Popen([NESASM_PY_BIN, 'asm', _input], cwd=path)
    p.wait()

class NESAsmCiTest(HexFileTestCase):

    def setUp(self):
        if not exists(NESASM_C_BIN):
            raise SkipTest('no NESASM bin')

    def prepare_scenario(self, _input, _output):
        from distutils.dir_util import copy_tree
        from shutil import rmtree
        if exists(_output):
            rmtree(_output)
        path = dirname(abspath(_input))
        filename = basename(_input)
        copy_tree(path, _output)

        for f in glob(_output + '/*.nes'):
            remove(f)

        return _output + '/' + filename

    def nesasm_c(self, _input):
        nesfile = splitext(_input)[0] + '.nes'
        self.assertFalse(exists(nesfile))
        nesasm_c(_input)
        self.assertTrue(exists(nesfile))
        return nesfile

    def nesasm_py(self, _input):
        nesfile = splitext(_input)[0] + '.nes'
        self.assertFalse(exists(nesfile))
        nesasm_py(_input)
        self.assertTrue(exists(nesfile))
        return nesfile

    def test_movingsprite(self):
        _input = 'fixtures/movingsprite/movingsprite.asm'
        _input_c = self.prepare_scenario(_input, '/tmp/nesasm_c')
        _input_py = self.prepare_scenario(_input, '/tmp/nesasm_py')

        _output_c = self.nesasm_c(_input_c)
        _output_py = self.nesasm_py(_input_py)

        self.assertHexFileEquals(_output_c, _output_py)
