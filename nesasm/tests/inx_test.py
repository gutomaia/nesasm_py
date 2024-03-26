import unittest

from nesasm.tests import MetaInstructionCase


class InxSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'INX'
    lex = [('T_INSTRUCTION', 'INX')]
    syn = ['S_IMPLIED']
    code = [0xe8]
