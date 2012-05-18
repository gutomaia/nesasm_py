# -*- coding: utf-8 -*-

import unittest

from pynes.compiler import lexical, syntax, semantic

class CpyTest(unittest.TestCase):

    def test_cpy_imm(self):
        tokens = lexical('CPY #10')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0xc0, 0x10])

    def test_cpy_zp(self):
        tokens = lexical('CPY $00')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0xc4, 0x00])

    def test_cpy_abs(self):
        tokens = lexical('CPY $1234')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        self.assertEquals('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0xcc, 0x34, 0x12])