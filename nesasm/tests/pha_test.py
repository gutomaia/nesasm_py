import unittest

from nesasm.tests import MetaInstructionCase


class PhaSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'PHA'
    lex = [('T_INSTRUCTION', 'PHA')]
    syn = ['S_IMPLIED']
    code = [0x48]
