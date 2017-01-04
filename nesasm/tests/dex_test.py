# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class DexSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'DEX'
    lex = [('T_INSTRUCTION', 'DEX')]
    syn = ['S_IMPLIED']
    code = [0xca]
