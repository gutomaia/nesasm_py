import unittest

from nesasm.cartridge import Cartridge


class CartridgeTest(unittest.TestCase):

    def setUp(self):
        self.cart = Cartridge()

    def tearDown(self):
        self.cart = None

    def test_inesprg_1(self):
        self.cart.set_iNES_prg(1)
        self.assertEqual(1, self.cart.inespgr)

    def test_inesprg_2(self):
        self.cart.set_iNES_prg(2)
        self.assertEqual(2, self.cart.inespgr)

    def test_ineschr(self):
        self.cart.set_iNES_chr(1)
        self.assertEqual(1, self.cart.ineschr)

    def test_inesmap(self):
        self.cart.set_iNES_map(1)
        self.assertEqual(1, self.cart.inesmap)

    def test_inesmir(self):
        self.cart.set_iNES_mir(1)
        self.assertEqual(1, self.cart.inesmir)

    def test_bank_1(self):
        self.cart.set_bank_id(0)
        self.assertEqual(1, len(self.cart.banks))

    def test_bank_2(self):
        self.cart.set_bank_id(0)
        self.cart.set_bank_id(1)
        self.assertEqual(2, len(self.cart.banks))

    def test_org_1(self):
        self.cart.set_bank_id(0)
        self.cart.set_org(0xc000)
        self.assertEqual(0xc000, self.cart.banks[0]['start'])

    def test_append_code(self):
        code = [0x4e, 0x45, 0x53, 0x1a]
        self.cart.append_code(code)
        self.assertEqual(4, self.cart.pc)
        self.assertEqual(code, self.cart.get_code())

    def test_using_org_to_jump(self):
        self.cart.set_bank_id(0)
        self.cart.set_org(0xc000)
        code = [0x4e, 0x45, 0x53, 0x1a]
        self.cart.append_code(code)
        self.cart.set_org(0xc000 + 8)
        self.cart.append_code(code)
        self.assertEqual(
            [0x4e, 0x45, 0x53, 0x1a, 0xff, 0xff,
                0xff, 0xff, 0x4e, 0x45, 0x53, 0x1a],
            self.cart.get_code()
        )
