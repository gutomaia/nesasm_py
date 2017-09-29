# -*- coding: utf-8 -*-
'''
CMP, Compare with Accumulator Test
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class CpmImmTest(unittest.TestCase):

    asm = 'CMP #$10'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xc9, 0x10]


@add_metaclass(MetaInstructionCase)
class CpmImmDecimalTest(unittest.TestCase):

    asm = 'CMP #10'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xc9, 0x0a]


@add_metaclass(MetaInstructionCase)
class CpmImmBinaryTest(unittest.TestCase):

    asm = 'CMP #%00000100'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xc9, 0x04]


@add_metaclass(MetaInstructionCase)
class CpmZpTest(unittest.TestCase):

    asm = 'CMP $00'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xc5, 0x00]


@add_metaclass(MetaInstructionCase)
class CpmZpxTest(unittest.TestCase):

    asm = 'CMP $10,X'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_ADDRESS', '$10'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ZEROPAGE_X']
    code = [0xd5, 0x10]


@add_metaclass(MetaInstructionCase)
class CpmAbsTest(unittest.TestCase):

    asm = 'CMP $1234'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xcd, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class CpmAbsxTest(unittest.TestCase):

    asm = 'CMP $1234, X'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X')]
    syn = ['S_ABSOLUTE_X']
    code = [0xdd, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class CpmAbsyTest(unittest.TestCase):

    asm = 'CMP $1234, Y'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_ADDRESS', '$1234'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'Y')]
    syn = ['S_ABSOLUTE_Y']
    code = [0xd9, 0x34, 0x12]


@add_metaclass(MetaInstructionCase)
class CpmIndxTest(unittest.TestCase):

    asm = 'CMP ($20, X)'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_OPEN', '('), ('T_ADDRESS', '$20'),
           ('T_SEPARATOR', ','), ('T_REGISTER', 'X'), ('T_CLOSE', ')')]
    syn = ['S_INDIRECT_X']
    code = [0xc1, 0x20]


@add_metaclass(MetaInstructionCase)
class CpmIndyTest(unittest.TestCase):

    asm = 'CMP ($20),Y'
    lex = [('T_INSTRUCTION', 'CMP'), ('T_OPEN', '('), ('T_ADDRESS', '$20'),
           ('T_CLOSE', ')'), ('T_SEPARATOR', ','), ('T_REGISTER', 'Y'), ]
    syn = ['S_INDIRECT_Y']
    code = [0xd1, 0x20]
