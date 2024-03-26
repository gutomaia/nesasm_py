import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class SecSnglTest(unittest.TestCase):
    asm = 'SEC'
    lex = [('T_INSTRUCTION', 'SEC')]
    syn = ['S_IMPLIED']
    code = [0x38]
