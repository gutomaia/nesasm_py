# -*- coding: utf-8 -*-
import unittest

from nesasm.compiler import lexical, syntax, semantic

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class ConstantAdcImmTest(unittest.TestCase):
    asm = 'FOO = #$10\nADC FOO'
    lex = [
        ('T_MARKER', 'FOO'),
        ('T_EQUAL', '='),
        ('T_HEX_NUMBER', '#$10'),
        ('T_ENDLINE', '\n'),
        ('T_INSTRUCTION', 'ADC'),
        ('T_MARKER', 'FOO'),
    ]

    syn = ['S_CONSTANT', 'S_IMMEDIATE']
    code = [0x69, 0x10]


@add_metaclass(MetaInstructionCase)
class ConstantAdcImmWithDecimalTest(unittest.TestCase):
    asm = 'FOO = #10\nADC FOO'
    lex = [
        ('T_MARKER', 'FOO'),
        ('T_EQUAL', '='),
        ('T_DECIMAL_NUMBER', '#10'),
        ('T_ENDLINE', '\n'),
        ('T_INSTRUCTION', 'ADC'),
        ('T_MARKER', 'FOO'),
    ]
    syn = ['S_CONSTANT', 'S_IMMEDIATE']
    code = [0x69, 0x0A]


@add_metaclass(MetaInstructionCase)
class ConstantAdcImmWithBinaryTest(unittest.TestCase):
    asm = 'FOO = #%00000100\nADC FOO'
    lex = [
        ('T_MARKER', 'FOO'),
        ('T_EQUAL', '='),
        ('T_BINARY_NUMBER', '#%00000100'),
        ('T_ENDLINE', '\n'),
        ('T_INSTRUCTION', 'ADC'),
        ('T_MARKER', 'FOO'),
    ]
    syn = ['S_CONSTANT', 'S_IMMEDIATE']
    code = [0x69, 0x04]


@add_metaclass(MetaInstructionCase)
class ConstantAdcZpTest(unittest.TestCase):
    asm = 'FOO = $00\nADC FOO'
    lex = [
        ('T_MARKER', 'FOO'),
        ('T_EQUAL', '='),
        ('T_ADDRESS', '$00'),
        ('T_ENDLINE', '\n'),
        ('T_INSTRUCTION', 'ADC'),
        ('T_MARKER', 'FOO'),
    ]
    syn = ['S_CONSTANT', 'S_ZEROPAGE']
    code = [0x65, 0x00]
