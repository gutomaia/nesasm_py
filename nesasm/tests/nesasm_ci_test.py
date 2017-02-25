from nesasm.tests import HexFileTestCase
from unittest import SkipTest
from os import remove, makedirs
from os.path import abspath, basename, dirname, exists, splitext
from glob import glob

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


def prepare_scenario(_input, _output):
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


class NESAsmCiSuite(object):

    @classmethod
    def setUpClass(cls):
        if not exists(NESASM_C_BIN):
            return
        _input = 'fixtures/%s' % cls.fixture

        _filename = splitext(basename(_input))[0]

        from sys import version_info
        version = '_'.join([str(c) for c in version_info[:3]])
        c_out = '/tmp/nesasm/%s/%s/nesasm_c' % (version, _filename)
        cls._input_c = prepare_scenario(_input, c_out)
        py_out = '/tmp/nesasm/%s/%s/nesasm_py' % (version, _filename)
        cls._input_py = prepare_scenario(_input, py_out)

    def setUp(self):
        if not exists(NESASM_C_BIN):
            raise SkipTest('no NESASM bin')

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

    def test_binary_compare(self):
        _output_c = self.nesasm_c(self._input_c)
        _output_py = self.nesasm_py(self._input_py)

        self.assertHexFileEquals(_output_c, _output_py)

    def test_compare_labels(self):
        labels_file = splitext(self._input_c)[0] + '.fns'
        labels_c = {}
        with open(labels_file, 'r') as f:
            for line in f:
                if not line.startswith(';'):
                    key, value = [d.strip() for d in line.split('=')]
                    labels_c[key] = value

        from nesasm.compiler import lexical, syntax, get_labels

        with open(self._input_py) as f:
            source = f.read()

        ast = syntax(lexical(source))
        try:
            _items = get_labels(ast).iteritems
        except AttributeError:
            _items = get_labels(ast).items

        labels_py = {k: '${:02X}'.format(v) for k, v in _items()}

        self.assertEquals(labels_c, labels_py)


class MovingspriteTest(NESAsmCiSuite, HexFileTestCase):
    fixture = 'movingsprite/movingsprite.asm'


class BackgroundTest(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/background/background.asm'


class Background3Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/background/background3.asm'


class Scrolling1Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/scrolling/scrolling1.asm'


class Scrolling2Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/scrolling/scrolling2.asm'


class Scrolling3Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/scrolling/scrolling3.asm'


class Scrolling4Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/scrolling/scrolling4.asm'


class Scrolling5Test(NESAsmCiSuite, HexFileTestCase):
    fixture = 'nerdynights/scrolling/scrolling5.asm'
