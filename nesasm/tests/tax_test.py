import unittest

from nesasm.tests import MetaInstructionCase


class TaxSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'TAX'
    lex = [('T_INSTRUCTION', 'TAX')]
    syn = ['S_IMPLIED']
    code = [0xaa]
