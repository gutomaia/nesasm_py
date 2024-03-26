import unittest

from nesasm.tests import MetaInstructionCase


class PlpSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'PLP'
    lex = [('T_INSTRUCTION', 'PLP')]
    syn = ['S_IMPLIED']
    code = [0x28]
