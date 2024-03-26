import unittest

from nesasm.tests import MetaInstructionCase


class RtiSnglTest(unittest.TestCase, metaclass=MetaInstructionCase):
    asm = 'RTI'
    lex = [('T_INSTRUCTION', 'RTI')]
    syn = ['S_IMPLIED']
    code = [0x40]
