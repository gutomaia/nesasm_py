import unittest

from nesasm.tests import MetaInstructionCase


class DexSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'DEX'
    lex = [('T_INSTRUCTION', 'DEX')]
    syn = ['S_IMPLIED']
    code = [0xca]
