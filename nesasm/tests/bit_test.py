# -*- coding: utf-8 -*-

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class BitZpTest(unittest.TestCase):

    asm = 'BIT $00'
    lex = [('T_INSTRUCTION', 'BIT'), ('T_ADDRESS', '$00')]
    syn = ['S_ZEROPAGE']
    code = [0x24, 0x00]


@add_metaclass(MetaInstructionCase)
class BitAbsTest(unittest.TestCase):

    asm = 'BIT $1234'
    lex = [('T_INSTRUCTION', 'BIT'), ('T_ADDRESS', '$1234')]
    syn = ['S_ABSOLUTE']
    code = [0x2c, 0x34, 0x12]
