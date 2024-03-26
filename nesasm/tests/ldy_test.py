'''
LDY, Load Register Y

This is one of the memory operations on the 6502
'''

import unittest
from nesasm.tests import MetaInstructionCase


class LdyImmTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY #$10'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x10]


class LdyImmDecimalTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY #10'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x0a]


class LdyImmBinaryTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY #%00000100'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xa0, 0x04]


class LdyZpTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY $00'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xa4, 0x00]


class LdyZpxTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY $10,X'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ZEROPAGE_X']
    code = [0xb4, 0x10]


class LdyAbsTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY $1234'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xac, 0x34, 0x12]


class LdyAbsxTest(unittest.TestCase, metaclass=MetaInstructionCase):

    asm = 'LDY $1234,X'
    lex = [('T_INSTRUCTION', 'LDY'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ABSOLUTE_X']
    code = [0xbc, 0x34, 0x12]
