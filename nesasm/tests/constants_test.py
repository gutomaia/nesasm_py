# -*- coding: utf-8 -*-
import unittest

from nesasm.compiler import lexical, syntax, semantic

import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class ConstantLdaAbs(unittest.TestCase):
    asm = 'JOYSTICK1 = $4016\nLDA JOYSTICK1'
    lex = [
        ('T_MARKER', 'JOYSTICK1'),
        ('T_EQUAL', '='),
        ('T_ADDRESS', '$4016'),
        ('T_ENDLINE', '\n'),
        ('T_INSTRUCTION', 'LDA'),
        ('T_MARKER', 'JOYSTICK1'),
    ]

    syn = ['S_CONSTANT', 'S_ABSOLUTE']
    code = [0xad, 0x16, 0x40]
