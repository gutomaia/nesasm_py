import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class DeySnglTest(unittest.TestCase):
    asm = 'DEY'
    lex = [('T_INSTRUCTION', 'DEY')]
    syn = ['S_IMPLIED']
    code = [0x88]
