# -*- coding: utf-8 -*-
'''
LDX, Load Register X

This is one of the memory operations on the 6502
'''
import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class LdxImmTest(unittest.TestCase):

    asm = 'LDX #$10'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xa2, 0x10]


@add_metaclass(MetaInstructionCase)
class LdxImmDecimalTest(unittest.TestCase):

    asm = 'LDX #10'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xa2, 0x0a]


@add_metaclass(MetaInstructionCase)
class LdxImmBinaryTest(unittest.TestCase):

    asm = 'LDX #%00000100'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xa2, 0x04]


@add_metaclass(MetaInstructionCase)
class LdxZpTest(unittest.TestCase):

    asm = 'LDX $00'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xa6, 0x00]


@add_metaclass(MetaInstructionCase)
class LdxZpyTest(unittest.TestCase):

    asm = 'LDX $10,Y'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'Y')]
    syn = ['S_ZEROPAGE_Y']
    code = [0xb6, 0x10]


@add_metaclass(MetaInstructionCase)
class LdxAbsTest(unittest.TestCase):

    asm = 'LDX $1234'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xae, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class LdxAbsyTest(unittest.TestCase):

    asm = 'LDX $1234,Y'
    lex = [('T_INSTRUCTION', 'LDX'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'Y')]
    syn = ['S_ABSOLUTE_Y']
    code = [0xbe, 0x34, 0x12]
