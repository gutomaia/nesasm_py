'''
BMI, Branch on Result Minus Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch
if N == 1.
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass

@add_metaclass(MetaInstructionCase)
class BmiRelTest(unittest.TestCase):

    asm = 'BMI $10'
    lex = [('T_INSTRUCTION', 'BMI'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0x30, 0x0e]
