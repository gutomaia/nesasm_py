'''
BEQ, Branch on Result Zero Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch
if Z == 1.
'''

import unittest
from nesasm.tests import MetaInstructionCase

class BeqRelTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'BEQ $10'
    lex = [('T_INSTRUCTION', 'BEQ'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0xf0, 0x0e]
