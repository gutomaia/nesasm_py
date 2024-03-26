import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class TyaSnglTest(unittest.TestCase):
    asm = 'TYA'
    lex = [('T_INSTRUCTION', 'TYA')]
    syn = ['S_IMPLIED']
    code = [0x98]
