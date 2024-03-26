import unittest
from nesasm.tests import MetaInstructionCase


class ClvImplTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'CLV'
    lex = [('T_INSTRUCTION', 'CLV')]
    syn = ['S_IMPLIED']
    code = [0xb8]
