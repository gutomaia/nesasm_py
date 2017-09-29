# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class DexSnglTest(unittest.TestCase):
    asm = 'DEX'
    lex = [('T_INSTRUCTION', 'DEX')]
    syn = ['S_IMPLIED']
    code = [0xca]
