import unittest

from nesasm.tests import MetaInstructionCase


class TsxSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'TSX'
    lex = [('T_INSTRUCTION', 'TSX')]
    syn = ['S_IMPLIED']
    code = [0xba]
