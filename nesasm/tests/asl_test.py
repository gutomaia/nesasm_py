# -*- coding: utf-8 -*-
'''
ASL, Arithmetic Shift Left

This is a test for the bit manipulation instruction ASL.
'''
import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass

@add_metaclass(MetaInstructionCase)
class AslImmTest(unittest.TestCase):
    # TODO see the accumulator type instruction, ASL A
    asm = 'ASL #$10'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0x0a, 0x10]


@add_metaclass(MetaInstructionCase)
class AslImmWithDecimal(unittest.TestCase):
    asm = 'ASL #10'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0x0a, 0x0A]


@add_metaclass(MetaInstructionCase)
class AslImmWithBinary(unittest.TestCase):
    asm = 'ASL #%00000100'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0x0a, 0x04]


@add_metaclass(MetaInstructionCase)
class AslZpTest(unittest.TestCase):
    asm = 'ASL $00'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0x06, 0x00]


@add_metaclass(MetaInstructionCase)
class AslZpxTest(unittest.TestCase):
    asm = 'ASL $10,X'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ZEROPAGE_X']
    code = [0x16, 0x10]


@add_metaclass(MetaInstructionCase)
class AslAbsTest(unittest.TestCase):
    asm = 'ASL $1234'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0x0e, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class AslAbsxTest(unittest.TestCase):
    asm = 'ASL $1234,X'
    lex = [('T_INSTRUCTION', 'ASL'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ABSOLUTE_X']
    code = [0x1e, 0x34, 0x12]
