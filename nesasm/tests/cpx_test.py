'''
CPX, Compare with X Test
'''

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class CpxImmTest(unittest.TestCase):

    asm = 'CPX #$10'
    lex = [('T_INSTRUCTION', 'CPX'), ('T_HEX_NUMBER', '#$10')]
    syn = ['S_IMMEDIATE']
    code = [0xe0, 0x10]


@add_metaclass(MetaInstructionCase)
class CpxImmDecimalTest(unittest.TestCase):

    asm = 'CPX #10'
    lex = [('T_INSTRUCTION', 'CPX'), ('T_DECIMAL_NUMBER', '#10')]
    syn = ['S_IMMEDIATE']
    code = [0xe0, 0x0a]


@add_metaclass(MetaInstructionCase)
class CpxImmBinaryTest(unittest.TestCase):

    asm = 'CPX #%00000100'
    lex = [('T_INSTRUCTION', 'CPX'), ('T_BINARY_NUMBER', '#%00000100')]
    syn = ['S_IMMEDIATE']
    code = [0xe0, 0x04]


@add_metaclass(MetaInstructionCase)
class CpxZpTest(unittest.TestCase):

    asm = 'CPX $00'
    lex = [('T_INSTRUCTION', 'CPX'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0xe4, 0x00]


@add_metaclass(MetaInstructionCase)
class CpxAbsTest(unittest.TestCase):

    asm = 'CPX $1234'
    lex = [('T_INSTRUCTION', 'CPX'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0xec, 0x34, 0x12]
