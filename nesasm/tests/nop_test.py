# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class NopSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'NOP'
    lex = [('T_INSTRUCTION', 'NOP')]
    syn = ['S_IMPLIED']
    code = [0xea]
