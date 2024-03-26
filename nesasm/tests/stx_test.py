import unittest

from nesasm.compiler import lexical, syntax, semantic


class StxTest(unittest.TestCase):

    def test_stx_zp(self):
        tokens = list(lexical('STX $00'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x86, 0x00])

    def test_stx_zpy(self):
        tokens = list(lexical('STX $10,Y'))
        self.assertEqual(4, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('T_SEPARATOR', tokens[2]['type'])
        self.assertEqual('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ZEROPAGE_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x96, 0x10])

    def test_stx_abs(self):
        tokens = list(lexical('STX $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x8e, 0x34, 0x12])
