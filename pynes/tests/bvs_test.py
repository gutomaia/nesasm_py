# -*- coding: utf-8 -*-
'''
BVS, Branch on Overflow Set Test

This is a test for the branch instruction BMI of
the 6502. This instruction performs the branch 
if V == 1.
'''

import unittest
from pynes.compiler import lexical, syntax, semantic


class BvsTest(unittest.TestCase):


    '''This is an relative instruction, so it works quite different
    from others. The instruction uses an offset witch can range from
    -128 to +127. The offset is added to the program counter.'''
    def test_bvs_rel(self):
        tokens = list(lexical('BVS $10'))
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_RELATIVE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x70, 0x0e])
