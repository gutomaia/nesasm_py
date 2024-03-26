import unittest
from types import GeneratorType
from nesasm.compiler import (lexical, syntax,
                             t_zeropage, t_address,
                             t_separator, get_labels)


class CompilerTest(unittest.TestCase):

    def setUp(self):
        self.zeropage = dict(
            type='T_ADDRESS',
            value='$00'
        )
        self.address10 = dict(
            type='T_ADDRESS',
            value='$1234'
        )
        self.separator = dict(
            type='T_SEPARATOR',
            value=','
        )

    def test_t_zeropage(self):
        self.assertTrue(t_zeropage([self.zeropage], 0))

    def test_t_address(self):
        self.assertTrue(t_address([self.address10], 0))

    def test_t_separator(self):
        self.assertTrue(t_separator([self.separator], 0))

    def test_compile_more_than_on_instruction(self):
        code = '''
            SEC         ;clear the carry
            LDA $20     ;get the low byte of the first number
            '''
        tokens = list(lexical(code))
        self.assertEqual(6, len(tokens))
        self.assertEqual('T_ENDLINE', tokens[0]['type'])
        self.assertEqual('T_INSTRUCTION', tokens[1]['type'])
        self.assertEqual('T_ENDLINE', tokens[2]['type'])
        self.assertEqual('T_INSTRUCTION', tokens[3]['type'])
        self.assertEqual('T_ADDRESS', tokens[4]['type'])
        self.assertEqual('T_ENDLINE', tokens[5]['type'])
        ast = syntax(tokens)
        self.assertEqual(2, len(ast))

    def test_compile_decimal(self):
        code = '''
            LDA #128
            STA $0203
        '''
        tokens = list(lexical(code))
        self.assertEqual(7, len(tokens))
        self.assertEqual('T_ENDLINE', tokens[0]['type'])
        self.assertEqual('T_INSTRUCTION', tokens[1]['type'])
        self.assertEqual('T_DECIMAL_NUMBER', tokens[2]['type'])
        self.assertEqual('T_ENDLINE', tokens[3]['type'])
        self.assertEqual('T_INSTRUCTION', tokens[4]['type'])
        self.assertEqual('T_ADDRESS', tokens[5]['type'])
        self.assertEqual('T_ENDLINE', tokens[6]['type'])

    def test_compile_list(self):
        code = '''
        palette:
          .db $0F,$01,$02,$03,$04,$05,$06,$07,$08,$09,$0A,$0B,$0C,$0D,$0E,$0F
          .db $0F,$30,$31,$32,$33,$35,$36,$37,$38,$39,$3A,$3B,$3C,$3D,$3E,$0F
        '''
        tokens = list(lexical(code))
        ast = syntax(tokens)
        self.assertEqual(2, len(ast))

        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        self.assertEqual('.db', ast[0]['children'][0]['value'])
        self.assertEqual(32, len(ast[0]['children']))
        palette1 = [0x0f, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                    0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
        for i, p in enumerate(palette1):
            h = '$%02X' % p
            self.assertEqual(h, ast[0]['children'][i * 2 + 1]['value'])
            self.assertEqual('S_DIRECTIVE', ast[1]['type'])

        self.assertEqual('S_DIRECTIVE', ast[1]['type'])
        self.assertEqual('.db', ast[0]['children'][0]['value'])
        self.assertEqual(32, len(ast[1]['children']))
        palette2 = [0x0f, 0x30, 0x31, 0x32, 0x33, 0x35, 0x36, 0x37, 0x38, 0x39,
                    0x3a, 0x3b, 0x3c, 0x3d, 0x3e, 0x0f]
        for i, p in enumerate(palette2):
            h = '$%02X' % p
            self.assertEqual(h, ast[1]['children'][i * 2 + 1]['value'])

    def test_instructions_with_labels(self):
        code = '''
              .org $C000

            WAITVBLANK:
              BIT $2002
              BPL WAITVBLANK
              RTS'''

        tokens = list(lexical(code))
        ast = syntax(tokens)
        self.assertEqual(4, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        self.assertEqual('S_ABSOLUTE', ast[1]['type'])
        self.assertEqual(['WAITVBLANK'], ast[1]['labels'])

        labels = get_labels(ast)
        expected = {'WAITVBLANK': 0xc000}

        self.assertEqual(expected, labels)

    def test_several_lists_with_labels(self):
        code = '''
        .org $E000

        palette:
          .db $0F,$01,$02,$03,$04,$05,$06,$07,$08,$09,$0A,$0B,$0C,$0D,$0E,$0F
          .db $0F,$30,$31,$32,$33,$35,$36,$37,$38,$39,$3A,$3B,$3C,$3D,$3E,$0F

        sprites:
          .db $80, $00, $03, $80; Y pos, tile id, attributes, X pos
        '''

        tokens = list(lexical(code))
        ast = syntax(tokens)
        self.assertEqual(4, len(ast))
        self.assertEqual('S_DIRECTIVE', ast[0]['type'])
        self.assertEqual('.org', ast[0]['children'][0]['value'])
        self.assertEqual('S_DIRECTIVE', ast[1]['type'])
        self.assertEqual('.db', ast[1]['children'][0]['value'])
        self.assertEqual(['palette'], ast[1]['labels'])

        self.assertEqual('S_DIRECTIVE', ast[2]['type'])
        self.assertEqual('.db', ast[2]['children'][0]['value'])

        self.assertEqual('S_DIRECTIVE', ast[3]['type'])
        self.assertEqual('.db', ast[3]['children'][0]['value'])
        self.assertEqual(['sprites'], ast[3]['labels'])

        labels = get_labels(ast)
        expected = {'palette': 0xE000, 'sprites': 0xE000 + 32}

        self.assertEqual(expected, labels)

    @unittest.skip('TODO:')
    def test_raise_erro_with_unknow_label(self):
        with self.assertRaises(Exception):
            tokens = lexical('LDA unknow')
            list(tokens)

    def test_lexical_returns_a_generator(self):
        tokens = lexical('BIT $00')
        self.assertIsInstance(tokens, GeneratorType)
