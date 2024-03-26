import unittest

from nesasm.tests import MetaInstructionCase


class TaySnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'TAY'
    lex = [('T_INSTRUCTION', 'TAY')]
    syn = ['S_IMPLIED']
    code = [0xa8]
