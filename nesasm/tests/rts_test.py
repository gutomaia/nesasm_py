import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class RtsSnglTest(unittest.TestCase):
    asm = 'RTS'
    lex = [('T_INSTRUCTION', 'RTS')]
    syn = ['S_IMPLIED']
    code = [0x60]
