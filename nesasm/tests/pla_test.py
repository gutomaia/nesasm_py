import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class PlaSnglTest(unittest.TestCase):
    asm = 'PLA'
    lex = [('T_INSTRUCTION', 'PLA')]
    syn = ['S_IMPLIED']
    code = [0x68]
