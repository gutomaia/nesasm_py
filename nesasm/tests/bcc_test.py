# -*- coding: utf-8 -*-
'''
BCC, Branch on Carry Clear Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch
if C == 0.
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass

@add_metaclass(MetaInstructionCase)
class BccRelTest(unittest.TestCase):

    asm = 'BCC $10'
    lex = [('T_INSTRUCTION', 'BCC'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0x90, 0x0e]
