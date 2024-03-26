import unittest

from nesasm.tests import MetaInstructionCase


class PhpSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'PHP'
    lex = [('T_INSTRUCTION', 'PHP')]
    syn = ['S_IMPLIED']
    code = [0x08]
