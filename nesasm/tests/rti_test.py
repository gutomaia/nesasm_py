import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class RtiSnglTest(unittest.TestCase):
    asm = 'RTI'
    lex = [('T_INSTRUCTION', 'RTI')]
    syn = ['S_IMPLIED']
    code = [0x40]
