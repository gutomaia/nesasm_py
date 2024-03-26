import unittest

from nesasm.compiler import lexical, syntax, semantic


class StaTest(unittest.TestCase):

    def test_sta_zp(self):
        tokens = list(lexical('STA $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x85, 0x00])

    def test_sta_zpx(self):
        tokens = list(lexical('STA $10,X'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x95, 0x10])

    def test_sta_abs(self):
        tokens = list(lexical('STA $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x8D, 0x34, 0x12])

    def test_sta_absx(self):
        tokens = list(lexical('STA $1234,X'))
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
        self.assertEqual(code, [0x9D, 0x34, 0x12])

    def test_sta_absy(self):
        tokens = list(lexical('STA $1234,Y'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x99, 0x34, 0x12])

    def test_sta_indx(self):
        tokens = list(lexical('STA ($20,X)'))
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
        self.assertEqual(code, [0x81, 0x20])

    def test_sta_indy(self):
        tokens = list(lexical('STA ($20),Y'))
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
        self.assertEqual(code, [0x91, 0x20])
