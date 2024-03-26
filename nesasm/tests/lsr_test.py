# -*- coding: utf-8 -*-
'''
LSR, Logical Shift Right Test

This is an Bit Manipulation operation of the 6502
'''

import unittest

from nesasm.compiler import lexical, syntax, semantic


class LsrTest(unittest.TestCase):

    def test_lsr_acc(self):
        tokens = list(lexical('LSR A'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ACCUMULATOR', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ACCUMULATOR', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4a])

    def test_lsr_imm(self):
        tokens = list(lexical('LSR #$10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4a, 0x10])

    def test_lsr_imm_with_decimal(self):
        tokens = list(lexical('LSR #10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4a, 0x0a])

    def test_lsr_imm_with_binary(self):
        tokens = list(lexical('LSR #%00000100'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_BINARY_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4a, 0x04])

    def test_lsr_zp(self):
        tokens = list(lexical('LSR $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x46, 0x00])

    def test_lsr_zpx(self):
        tokens = list(lexical('LSR $10,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x56, 0x10])

    def test_lsr_abs(self):
        tokens = list(lexical('LSR $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4e, 0x34, 0x12])

    def test_lsr_absx(self):
        tokens = list(lexical('LSR $1234,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x5e, 0x34, 0x12])
