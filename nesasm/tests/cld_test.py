import unittest
from nesasm.tests import MetaInstructionCase


class CldImplTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'CLD'
    lex = [('T_INSTRUCTION', 'CLD')]
    syn = ['S_IMPLIED']
    code = [0xd8]
