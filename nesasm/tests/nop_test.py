import unittest

from nesasm.tests import MetaInstructionCase


class NopSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'NOP'
    lex = [('T_INSTRUCTION', 'NOP')]
    syn = ['S_IMPLIED']
    code = [0xea]
