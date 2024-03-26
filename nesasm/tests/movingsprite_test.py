# -*- coding: utf-8 -*-
from nesasm.tests import HexTestCase
from nesasm.compiler import lexical, syntax, semantic, get_labels
from nesasm.cartridge import Cartridge


class MovingSpriteTest(HexTestCase):

    def __init__(self, testname):
        HexTestCase.__init__(self, testname)
        f = open('fixtures/movingsprite/movingsprite.asm')
        code = f.read()
        f.close()
        tokens = lexical(code)
        self.ast = syntax(tokens)

    def test_inesprg_1(self):
        self.assertEqual('S_DIRECTIVE', self.ast[0]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[0]['children'][0]['type'])
        self.assertEqual('.inesprg', self.ast[0]['children'][0]['value'])
        self.assertEqual(5, self.ast[0]['children'][0]['line'])
        self.assertEqual(3, self.ast[0]['children'][0]['column'])

    def test_ineschr_1(self):
        self.assertEqual('S_DIRECTIVE', self.ast[1]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[1]['children'][0]['type'])
        self.assertEqual('.ineschr', self.ast[1]['children'][0]['value'])
        self.assertEqual(6, self.ast[1]['children'][0]['line'])
        self.assertEqual(3, self.ast[1]['children'][0]['column'])

    def test_inesmap_0(self):
        self.assertEqual('S_DIRECTIVE', self.ast[2]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[2]['children'][0]['type'])
        self.assertEqual('.inesmap', self.ast[2]['children'][0]['value'])
        self.assertEqual(7, self.ast[2]['children'][0]['line'])
        self.assertEqual(3, self.ast[2]['children'][0]['column'])

    def test_inesmir_1(self):
        self.assertEqual('S_DIRECTIVE', self.ast[3]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[3]['children'][0]['type'])
        self.assertEqual('.inesmir', self.ast[3]['children'][0]['value'])
        self.assertEqual(8, self.ast[3]['children'][0]['line'])
        self.assertEqual(3, self.ast[3]['children'][0]['column'])

    def test_bank_0(self):
        self.assertEqual('S_DIRECTIVE', self.ast[4]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[4]['children'][0]['type'])
        self.assertEqual('.bank', self.ast[4]['children'][0]['value'])
        self.assertEqual(11, self.ast[4]['children'][0]['line'])
        self.assertEqual(3, self.ast[4]['children'][0]['column'])

    def test_org_c0000(self):
        self.assertEqual('S_DIRECTIVE', self.ast[5]['type'])
        self.assertEqual('T_DIRECTIVE', self.ast[5]['children'][0]['type'])
        self.assertEqual('.org', self.ast[5]['children'][0]['value'])
        self.assertEqual(12, self.ast[5]['children'][0]['line'])
        self.assertEqual(3, self.ast[5]['children'][0]['column'])

    def test_waitvblank_bit_2002(self):
        self.assertEqual('S_ABSOLUTE', self.ast[6]['type'])
        self.assertEqual(['WAITVBLANK'], self.ast[6]['labels'])
        self.assertEqual('T_INSTRUCTION', self.ast[6]['children'][0]['type'])
        self.assertEqual('BIT', self.ast[6]['children'][0]['value'])
        self.assertEqual(15, self.ast[6]['children'][0]['line'])
        self.assertEqual(3, self.ast[6]['children'][0]['column'])

    def test_bpl_waitvblank(self):
        self.assertEqual('S_RELATIVE', self.ast[7]['type'])
        self.assertFalse('labels' in self.ast[7])
        self.assertEqual('T_INSTRUCTION', self.ast[7]['children'][0]['type'])
        self.assertEqual('BPL', self.ast[7]['children'][0]['value'])
        self.assertEqual(16, self.ast[7]['children'][0]['line'])
        self.assertEqual(3, self.ast[7]['children'][0]['column'])

    def test_rts(self):
        self.assertEqual('S_IMPLIED', self.ast[8]['type'])
        self.assertFalse('labels' in self.ast[8])
        self.assertEqual('T_INSTRUCTION', self.ast[8]['children'][0]['type'])
        self.assertEqual('RTS', self.ast[8]['children'][0]['value'])
        self.assertEqual(17, self.ast[8]['children'][0]['line'])
        self.assertEqual(3, self.ast[8]['children'][0]['column'])

    def test_asm_compiler(self):
        cart = Cartridge()
        cart.path = 'fixtures/movingsprite/'

        opcodes = semantic(self.ast, True, cart=cart)

        self.assertIsNotNone(opcodes)
        _bin = bytearray(opcodes)
        f = open('fixtures/movingsprite/movingsprite.nes', 'rb')
        content = f.read()
        f.close()
        self.assertHexEquals(content, _bin)

    def test_get_labels(self):
        expected = {}
        expected['WAITVBLANK'] = 0xC000
        expected['palette'] = 0xE000
        expected['sprites'] = 0xE000 + 32
        actual = get_labels(self.ast)
        self.assertEqual(expected['WAITVBLANK'], actual['WAITVBLANK'])
        self.assertEqual(expected['palette'], actual['palette'])
        self.assertEqual(expected['sprites'], actual['sprites'])
