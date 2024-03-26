import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class CliImplTest(unittest.TestCase):

    asm = 'CLI'
    lex = [('T_INSTRUCTION', 'CLI')]
    syn = ['S_IMPLIED']
    code = [0x58]
