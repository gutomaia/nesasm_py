# -*- coding: utf-8 -*-
'''
SBC, Subtract with Carry Test

This is an arithmetic instruction of the 6502.
'''
import unittest

from nesasm.compiler import lexical, syntax, semantic


class SbcTest(unittest.TestCase):

    def test_sbc_imm(self):
        tokens = list(lexical('SBC #$10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xe9, 0x10])

    def test_sbc_imm_with_decimal(self):
        tokens = list(lexical('SBC #10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xe9, 0x0a])

    def test_sbc_imm_with_binary(self):
        tokens = list(lexical('SBC #%00000100'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_BINARY_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xe9, 0x04])

    def test_sbc_zp(self):
        tokens = list(lexical('SBC $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xe5, 0x00])

    def test_sbc_zpx(self):
        tokens = list(lexical('SBC $10,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xf5, 0x10])

    def test_sbc_abs(self):
        tokens = list(lexical('SBC $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xed, 0x34, 0x12])

    def test_sbc_absx(self):
        tokens = list(lexical('SBC $1234,X'))
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
        self.assertEqual(code, [0xfd, 0x34, 0x12])

    def test_sbc_absy(self):
        tokens = list(lexical('SBC $1234,Y'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xf9, 0x34, 0x12])

    def test_sbc_indx(self):
        tokens = list(lexical('SBC ($20,X)'))
        self.assertEqual(6, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_OPEN', tokens[1]['type'])
        self.assertEqual('T_ADDRESS', tokens[2]['type'])
        self.assertEqual('$20', tokens[2]['value'])
        self.assertEqual('T_SEPARATOR', tokens[3]['type'])
        self.assertEqual('T_REGISTER', tokens[4]['type'])
        self.assertEqual('T_CLOSE', tokens[5]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_INDIRECT_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xe1, 0x20])

    def test_sbc_indy(self):
        tokens = list(lexical('SBC ($20),Y'))
        self.assertEqual(6, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_OPEN', tokens[1]['type'])
        self.assertEqual('T_ADDRESS', tokens[2]['type'])
        self.assertEqual('T_CLOSE', tokens[3]['type'])
        self.assertEqual('T_SEPARATOR', tokens[4]['type'])
        self.assertEqual('T_REGISTER', tokens[5]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_INDIRECT_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0xf1, 0x20])
