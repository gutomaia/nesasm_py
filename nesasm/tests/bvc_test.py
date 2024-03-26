'''
BVC, Branch on Overflow Clear Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch
if V == 0.
'''

import unittest
from nesasm.tests import MetaInstructionCase

class BvcRelTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'BVC $10'
    lex = [('T_INSTRUCTION', 'BVC'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0x50, 0x0e]
