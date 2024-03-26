'''
ROR, Rotate Right Test

This is an Bit Manipulation of the 6502.

'''

import unittest

from nesasm.compiler import lexical, syntax, semantic


class RorTest(unittest.TestCase):

    def test_ror_imm(self):
        tokens = list(lexical('ROR #$10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x6a, 0x10])

    def test_ror_imm_with_decimal(self):
        tokens = list(lexical('ROR #10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x6a, 0x0a])

    def test_ror_imm_with_binary(self):
        tokens = list(lexical('ROR #%00000100'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_BINARY_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x6a, 0x04])

    def test_ror_zp(self):
        tokens = list(lexical('ROR $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x66, 0x00])

    def test_ror_zpx(self):
        tokens = list(lexical('ROR $10,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x76, 0x10])

    def test_ror_abs(self):
        tokens = list(lexical('ROR $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x6e, 0x34, 0x12])

    def test_ror_absx(self):
        tokens = list(lexical('ROR $1234,X'))
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
        self.assertEqual(code, [0x7e, 0x34, 0x12])
