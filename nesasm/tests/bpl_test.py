'''
BPL, Branch on Result Plus Test

This is a test for the branch instruction BPL of
the 6502. This instruction performs the branch
if N == 0.
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass

@add_metaclass(MetaInstructionCase)
class BplRelTest(unittest.TestCase):

    asm = 'BPL $10'
    lex = [('T_INSTRUCTION', 'BPL'), ('T_ADDRESS', '$10')]
    syn = ['S_RELATIVE']
    code = [0x10, 0x0e]
