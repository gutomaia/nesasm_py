import unittest
from nesasm.tests import MetaInstructionCase


class CliImplTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'CLI'
    lex = [('T_INSTRUCTION', 'CLI')]
    syn = ['S_IMPLIED']
    code = [0x58]
