import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class SeiSnglTest(unittest.TestCase):
    asm = 'SEI'
    lex = [('T_INSTRUCTION', 'SEI')]
    syn = ['S_IMPLIED']
    code = [0x78]
