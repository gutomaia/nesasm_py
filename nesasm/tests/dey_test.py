import unittest

from nesasm.tests import MetaInstructionCase


class DeySnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'DEY'
    lex = [('T_INSTRUCTION', 'DEY')]
    syn = ['S_IMPLIED']
    code = [0x88]
