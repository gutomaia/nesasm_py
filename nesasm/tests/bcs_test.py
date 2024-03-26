'''
BCS, Branch on Carry Set Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch
if C == 0.
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass

@add_metaclass(MetaInstructionCase)
class BcsRelTest(unittest.TestCase):

    asm = 'BCS $10'
    lex = [('T_INSTRUCTION', 'BCS'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0xb0, 0x0e]
