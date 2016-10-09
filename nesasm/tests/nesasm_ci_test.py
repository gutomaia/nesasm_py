from nesasm.tests import HexFileTestCase
from unittest import SkipTest, skip
from os import devnull, remove, makedirs
from os.path import abspath, basename, dirname, exists, splitext
from glob import glob
import sys

NESASM_C_BIN = abspath('tools/nesasm/bin/nesasm')
NESASM_PY_BIN = abspath('bin/nesasm')


def call(*args):
    from subprocess import Popen, PIPE, STDOUT
    path = dirname(args[-1])
    p = Popen(args,
        stdin=PIPE, stdout=PIPE, stderr=PIPE,
        close_fds=True,
        cwd=path)
    exitcode = p.wait()
    if exitcode != 0:
        raise Exception('Exitcode %s: %s' % (exitcode, p.stderr.read()))


def nesasm_c(_input):
    call(NESASM_C_BIN, _input)


def nesasm_py(_input):
    call(NESASM_PY_BIN, 'asm', _input)


class NESAsmCiTest(HexFileTestCase):

    def setUp(self):
        if not exists(NESASM_C_BIN):
            raise SkipTest('no NESASM bin')

    def prepare_scenario(self, _input, _output):
        from distutils.dir_util import copy_tree
        from shutil import rmtree
        if exists(_output):
            rmtree(_output)
        makedirs(_output)
        path = dirname(abspath(_input))
        filename = basename(_input)
        copy_tree(path, _output)

        for f in glob(_output + '/*.nes'):
            remove(f)

        return _output + '/' + filename

    def nesasm_c(self, _input):
        nesfile = splitext(_input)[0] + '.nes'
        self.assertFalse(exists(nesfile), nesfile)
        nesasm_c(_input)
        self.assertTrue(exists(nesfile), nesfile)
        return nesfile

    def nesasm_py(self, _input):
        nesfile = splitext(_input)[0] + '.nes'
        self.assertFalse(exists(nesfile), nesfile)
        nesasm_py(_input)
        self.assertTrue(exists(nesfile), nesfile)
        return nesfile

    def binary_compare(self, fixture):
        _input = 'fixtures/%s' % fixture

        _filename = splitext(basename(_input))[0]

        from sys import version_info
        version = '_'.join([str(c) for c in version_info[:3]])

        _input_c = self.prepare_scenario(_input,
            '/tmp/nesasm/%s/%s/nesasm_c' % (version, _filename))
        _input_py = self.prepare_scenario(_input,
            '/tmp/nesasm/%s/%s/nesasm_py' % (version, _filename))

        _output_c = self.nesasm_c(_input_c)
        _output_py = self.nesasm_py(_input_py)

        self.assertHexFileEquals(_output_c, _output_py)


    def test_movingsprite(self):
        self.binary_compare('movingsprite/movingsprite.asm')

    def test_background(self):
        self.binary_compare('nerdynights/background/background.asm')

    def test_background3(self):
        self.binary_compare('nerdynights/background/background3.asm')

    def test_scrolling1(self):
        self.binary_compare('nerdynights/scrolling/scrolling1.asm')

    def test_scrolling2(self):
        self.binary_compare('nerdynights/scrolling/scrolling2.asm')

    def test_scrolling3(self):
        self.binary_compare('nerdynights/scrolling/scrolling3.asm')

    def test_scrolling4(self):
        self.binary_compare('nerdynights/scrolling/scrolling4.asm')

    def test_scrolling5(self):
        self.binary_compare('nerdynights/scrolling/scrolling5.asm')
