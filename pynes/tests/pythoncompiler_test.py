import unittest
from pynes.composer import pynes_compiler

class PythonTest(unittest.TestCase):


    def test_assign(self):
        opcode = pynes_compiler('a = 10')

    def test_binop_5_plus_3(self):
        return
        asm = pynes_compiler('5 + 3')
        self.assertIsNotNone(asm)
        expected = '''; Generated by pyNES
    PHA #05
    ADC #03'''

    def test_if_stmt_1(self):
        return
        if_stmt = '''
a = 0
if a!=80:
    a += 1
else:
    a -= 1
'''
        asm = pynes_compiler(if_stmt)
        expected = '''; Generated by pyNES
    CMP a, 80
    JNE notequal
    INC a
    JMP done
notequal:
    DEC a
done:'''
        #self.assertEquals(expected, asm)




    def test_if_stmt(self):
        return 
        if_stmt = '''
if True:
    return 1
else:
    return 2'''
        asm = pynes_compiler(if_stmt)

