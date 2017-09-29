# -*- coding: utf-8 -*-
'''
ADC, Add with Carry Test

This is an arithmetic instruction of the 6502.
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class AdcImmTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between decimal 16
    and the content of the accumulator.
    '''
    asm = 'ADC #$10'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0x69, 0x10]


@add_metaclass(MetaInstructionCase)
class AdcImmWithDecimalTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between decimal 10
    and the content of the accumulator.
    '''
    asm = 'ADC #10'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0x69, 0x0A]


@add_metaclass(MetaInstructionCase)
class AdcImmWithBinaryTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between binary %00000100
    (Decimal 4) and the content of the accumulator.
    '''
    asm = 'ADC #%00000100'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0x69, 0x04]


@add_metaclass(MetaInstructionCase)
class AdcZpTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between the content of
    the accumulator and the content of the zero page address.
    '''
    asm = 'ADC $00'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0x65, 0x00]


@add_metaclass(MetaInstructionCase)
class AdcZpxTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between the content of the
    accumulator and the content of the zero page with address
    calculated from $10 adding content of X.
    '''
    asm = 'ADC $10,X'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ZEROPAGE_X']
    code = [0x75, 0x10]


@add_metaclass(MetaInstructionCase)
class AdcAbsTest(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between the content of
    the accumulator and the content located at address $1234.
    '''
    asm = 'ADC $1234'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0x6d, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class AdcAbsx(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between the content of the
    accumulator and the content located at address $1234
    adding the content of X.
    '''
    asm = 'ADC $1234,X'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ABSOLUTE_X']
    code = [0x7d, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class AdcAbsy(unittest.TestCase):
    '''
    Test the arithmetic operation ADC between the content of the
    accumulator and the content located at address $1234
    adding the content of Y.
    '''
    asm = 'ADC $1234,Y'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'Y')]
    syn = ['S_ABSOLUTE_Y']
    code = [0x79, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class AdcIndx(unittest.TestCase):
    '''
    Test the arithmetic ADC operation between the content of the
    accumulator and the content located at the address
    obtained from the address calculated from the value
    stored in the address $20 adding the content of Y.
    '''
    asm = 'ADC ($20,X)'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_OPEN', '('),
           ('T_ADDRESS', '$20'), ('T_SEPARATOR', ','),
           ('T_REGISTER', 'X'), ('T_CLOSE', ')')]
    syn = ['S_INDIRECT_X']
    code = [0x61, 0x20]


@add_metaclass(MetaInstructionCase)
class AdcIndy(unittest.TestCase):
    '''
    Test arithmetic operation ADC between the content of the
    accumulator and the content located at the address
    obtained from the address calculated from the value
    stored in the address $20 adding the content of Y.
    '''
    asm = 'ADC ($20),Y'
    lex = [('T_INSTRUCTION', 'ADC'), ('T_OPEN', '('),
           ('T_ADDRESS', '$20'), ('T_CLOSE', ')'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'Y')]
    syn = ['S_INDIRECT_Y']
    code = [0x71, 0x20]
