'''
ORA, OR with Accumulator Test

This is an Logical operation of the 6502
'''

import unittest

from nesasm.compiler import lexical, syntax, semantic


class OraTest(unittest.TestCase):

    def test_ora_imm(self):
        '''Test logical OR operation between $10 (Decimal 16) and the
        content of the Accumulator'''
        tokens = list(lexical('ORA #$10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x09, 0x10])

    def test_ora_imm_with_decimal(self):
        '''Test logical OR operation between #10 (Decimal 10) and the
        content of the Accumulator'''
        tokens = list(lexical('ORA #10'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x09, 0x0a])

    def test_ora_imm_with_binary(self):
        '''Test logical OR operation between binary #%00000100
        (Decimal 4) and the content of the Accumulator'''
        tokens = list(lexical('ORA #%00000100'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_BINARY_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x09, 0x04])

    def test_ora_zp(self):
        '''Test logical OR operation between the content of the
        Accumulator and the content of zero page $00'''
        tokens = list(lexical('ORA $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x05, 0x00])

    def test_ora_zpx(self):
        tokens = list(lexical('ORA $10,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x15, 0x10])

    def test_ora_abs(self):
        tokens = list(lexical('ORA $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x0d, 0x34, 0x12])

    def test_ora_absx(self):
        tokens = list(lexical('ORA $1234,X'))
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
        self.assertEqual(code, [0x1d, 0x34, 0x12])

    def test_ora_absy(self):
        tokens = list(lexical('ORA $1234,Y'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x19, 0x34, 0x12])

    def test_ora_indx(self):
        tokens = list(lexical('ORA ($20,X)'))
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
        self.assertEqual(code, [0x01, 0x20])

    def test_ora_indy(self):
        tokens = list(lexical('ORA ($20),Y'))
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
        self.assertEqual(code, [0x11, 0x20])
