# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class NopSnglTest(unittest.TestCase):
    asm = 'NOP'
    lex = [('T_INSTRUCTION', 'NOP')]
    syn = ['S_IMPLIED']
    code = [0xea]
