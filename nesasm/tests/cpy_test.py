# -*- coding: utf-8 -*-
'''
CPY, Compare with Y Test

'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class CpyImmTest(unittest.TestCase):

    asm = 'CPY #$10'
    lex = [('T_INSTRUCTION', 'CPY'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xc0, 0x10]


@add_metaclass(MetaInstructionCase)
class CpyImmDecimalTest(unittest.TestCase):

    asm = 'CPY #10'
    lex = [('T_INSTRUCTION', 'CPY'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xc0, 0x0a]


@add_metaclass(MetaInstructionCase)
class CpyImmBinaryTest(unittest.TestCase):

    asm = 'CPY #%00000100'
    lex = [('T_INSTRUCTION', 'CPY'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xc0, 0x04]


@add_metaclass(MetaInstructionCase)
class CpyZpTest(unittest.TestCase):

    asm = 'CPY $00'
    lex = [('T_INSTRUCTION', 'CPY'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xc4, 0x00]


@add_metaclass(MetaInstructionCase)
class CpyAbsTest(unittest.TestCase):

    asm = 'CPY $1234'
    lex = [('T_INSTRUCTION', 'CPY'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xcc, 0x34, 0x12]
