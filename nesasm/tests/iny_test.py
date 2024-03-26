import unittest

from nesasm.tests import MetaInstructionCase


class InySnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'INY'
    lex = [('T_INSTRUCTION', 'INY')]
    syn = ['S_IMPLIED']
    code = [0xc8]
