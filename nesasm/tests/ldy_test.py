# -*- coding: utf-8 -*-
'''
LDY, Load Register Y

This is one of the memory operations on the 6502
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class LdyImmTest(unittest.TestCase):

    asm = 'LDY #$10'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x10]


@add_metaclass(MetaInstructionCase)
class LdyImmDecimalTest(unittest.TestCase):

    asm = 'LDY #10'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x0a]


@add_metaclass(MetaInstructionCase)
class LdyImmBinaryTest(unittest.TestCase):

    asm = 'LDY #%00000100'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x04]


@add_metaclass(MetaInstructionCase)
class LdyZpTest(unittest.TestCase):

    asm = 'LDY $00'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xa4, 0x00]


@add_metaclass(MetaInstructionCase)
class LdyZpxTest(unittest.TestCase):

    asm = 'LDY $10,X'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ZEROPAGE_X']
    code = [0xb4, 0x10]


@add_metaclass(MetaInstructionCase)
class LdyAbsTest(unittest.TestCase):

    asm = 'LDY $1234'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xac, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class LdyAbsxTest(unittest.TestCase):

    asm = 'LDY $1234,X'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ABSOLUTE_X']
    code = [0xbc, 0x34, 0x12]
