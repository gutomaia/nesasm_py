import unittest

from nesasm.tests import MetaInstructionCase


class TyaSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'TYA'
    lex = [('T_INSTRUCTION', 'TYA')]
    syn = ['S_IMPLIED']
    code = [0x98]
