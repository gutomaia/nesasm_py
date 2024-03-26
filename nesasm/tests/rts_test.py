import unittest

from nesasm.tests import MetaInstructionCase


class RtsSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'RTS'
    lex = [('T_INSTRUCTION', 'RTS')]
    syn = ['S_IMPLIED']
    code = [0x60]
