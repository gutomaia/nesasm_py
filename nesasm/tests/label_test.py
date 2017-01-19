from unittest import TestCase
from unittest import skip

from nesasm.compiler import lexical, get_labels, syntax, Cartridge


class LabelTest(TestCase):

    def get_labels(self, source, start_addr=0):
        cart = Cartridge()
        if start_addr != 0:
            cart.set_org(start_addr)
        return get_labels(syntax(lexical(source)), cart)


    def test_waitvblank_label(self):
        code = '''
            WAITVBLANK:
              BIT $2002
              BPL WAITVBLANK
              RTS
        '''

        labels = self.get_labels(code)
        self.assertEquals(labels['WAITVBLANK'], 0)

    def test_waitvblank_label_org_at_0x0100(self):
        code = '''
            .org 0100
            WAITVBLANK:
              BIT $2002
              BPL WAITVBLANK
              RTS
        '''

        labels = self.get_labels(code)
        self.assertEquals(labels['WAITVBLANK'], 256)

    def test_waitvblank_label_cartridge_at_0x0100(self):
        code = '''
            WAITVBLANK:
              BIT $2002
              BPL WAITVBLANK
              RTS
        '''

        labels = self.get_labels(code, 0x0100)
        self.assertEquals(labels['WAITVBLANK'], 256)
