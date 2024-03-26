'''
CLC, Clear Carry

This is a test for the clear carry instruction
'''


import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class ClsImplTest(unittest.TestCase):

    asm = 'CLC'
    lex = [('T_INSTRUCTION', 'CLC')]
    syn = ['S_IMPLIED']
    code = [0x18]
