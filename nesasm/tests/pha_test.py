import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class PhaSnglTest(unittest.TestCase):
    asm = 'PHA'
    lex = [('T_INSTRUCTION', 'PHA')]
    syn = ['S_IMPLIED']
    code = [0x48]
