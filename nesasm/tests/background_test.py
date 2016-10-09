# -*- coding: utf-8 -*-
from nesasm.tests import HexTestCase
from nesasm.compiler import lexical, syntax, semantic
from nesasm.cartridge import Cartridge
from unittest import skip


class BackgroundTest(HexTestCase):

    def __init__(self, testname):
        HexTestCase.__init__(self, testname)

    def assertAsmResults(self, source_file, bin_file):
        path = 'fixtures/nerdynights/background/'
        f = open(path + source_file)
        code = f.read()
        f.close()
        tokens = lexical(code)
        ast = syntax(tokens)

        cart = Cartridge()
        cart.path = 'fixtures/nerdynights/background/'

        opcodes = semantic(ast, True, cart=cart)

        self.assertIsNotNone(opcodes)
        bin = bytearray(opcodes)

        with open(path + bin_file, 'rb') as f:
            content = f.read()

        self.assertHexEquals(content, bin)

    def test_asm_compiler_background(self):
        self.assertAsmResults('background.asm', 'background.nes')

    def test_asm_compiler_background3(self):
        self.assertAsmResults('background3.asm', 'background3.nes')
