import unittest
from nesasm.compiler import lexical, syntax, semantic

# TODO: from pynes.asm import get_var


class DirectiveTest(unittest.TestCase):

    def test_label(self):
        tokens = list(lexical('label:'))
        self.assertEqual(1, len(tokens))
        self.assertEqual('T_LABEL', tokens[0]['type'])
        # ast = syntax(tokens)
        # self.assertEqual(1 , len(ast))

    def test_inesprg(self):
        tokens = list(lexical('.inesprg 1'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_ARGUMENT', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast, True)
        # self.assertEqual(1, get_var('inesprg'))
        self.assertEqual(code[4], 1)

    def test_ineschr(self):
        tokens = list(lexical('.ineschr 1'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_ARGUMENT', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast, True)
        # self.assertEqual(1, get_var('ineschr'))
        self.assertEqual(code[5], 1)

    def test_inesmap(self):
        tokens = list(lexical('.inesmap 1'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_ARGUMENT', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast, True)
        # self.assertEqual(1, get_var('inesmap'))
        self.assertEqual(code[6], 1)

    def test_inesmir(self):
        tokens = list(lexical('.inesmir 1'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_ARGUMENT', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast, True)
        # self.assertEqual(1, get_var('inesmir'))
        self.assertEqual(code[7], 1)

    def test_bank_0(self):
        tokens = list(lexical('.bank 0'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_DECIMAL_ARGUMENT', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        # code = semantic(ast)

    def test_org_0000(self):
        tokens = list(lexical('.org $0000'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        # code = semantic(ast)
        # self.assertEqual(0x0000, get_pc())

    def test_org_c000(self):
        tokens = list(lexical('.org $C000'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        # code = semantic(ast)
        # self.assertEqual(0xc000, get_pc())

    def test_org_fffa(self):
        tokens = list(lexical('.org $FFFA'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        # code = semantic(ast)
        # self.assertEqual(0xfffa, get_pc())

    def test_db_1(self):
        code = ('.db $0F,$01,$02,$03,$04,$05,$06,$07,'  # One-liner string
                '    $08,$09,$0A,$0B,$0C,$0D,$0E,$0F')
        tokens = list(lexical(code))
        self.assertEqual(32, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        # self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertIsNotNone(code)
        expected = [
            0x0f, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
            0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F
        ]
        self.assertEqual(expected, code)

    def test_db_2(self):
        code = ('.db $0F,$30,$31,$32,$33,$35,$36,$37,'  # One-liner string
                '    $38,$39,$3A,$3B,$3C,$3D,$3E,$0F')
        tokens = list(lexical(code))
        self.assertEqual(32, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        # self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertIsNotNone(code)
        expected = [0x0f, 0x30, 0x31, 0x32, 0x33, 0x35, 0x36, 0x37, 0x38,
                    0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x0F]
        self.assertEqual(expected, code)

    def test_db_3(self):
        tokens = list(lexical('.db $80, $00, $03, $80'))
        self.assertEqual(8, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        # self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertIsNotNone(code)
        expected = [0x80, 0x0, 0x03, 0x80]
        self.assertEqual(expected, code)

    def test_db_4(self):
        code = '''.db $80, $00, $03, $80
        .db $01, $02, $03, $04
        '''
        tokens = list(lexical(code))
        self.assertEqual(18, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        # self.assertEqual('T_HEX_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(2, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertIsNotNone(code)
        expected = [0x80, 0x0, 0x03, 0x80, 1, 2, 3, 4]
        self.assertEqual(expected, code)

    def test_db_5_with_binary(self):
        code = ('.db %00000000, %00010000, %01010000, '
                '%00010000, %00000000, %00000000, '
                '%00000000, %00110000')
        tokens = list(lexical(code))
        self.assertEqual(16, len(tokens))
        self.assertEqual('T_DIRECTIVE', tokens[0]['type'])
        self.assertEqual('T_BINARY_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertIsNotNone(code)
        expected = [0x00, 0x10, 0x50, 0x10, 0x00, 0x00, 0x00, 0x30]
        self.assertEqual(expected, code)
