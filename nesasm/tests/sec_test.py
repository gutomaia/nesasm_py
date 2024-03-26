import unittest

from nesasm.tests import MetaInstructionCase


class SecSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'SEC'
    lex = [('T_INSTRUCTION', 'SEC')]
    syn = ['S_IMPLIED']
    code = [0x38]
