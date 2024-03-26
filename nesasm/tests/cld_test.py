import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class CldImplTest(unittest.TestCase):

    asm = 'CLD'
    lex = [('T_INSTRUCTION', 'CLD')]
    syn = ['S_IMPLIED']
    code = [0xd8]
