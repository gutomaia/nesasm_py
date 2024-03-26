import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class InxSnglTest(unittest.TestCase):
    asm = 'INX'
    lex = [('T_INSTRUCTION', 'INX')]
    syn = ['S_IMPLIED']
    code = [0xe8]
