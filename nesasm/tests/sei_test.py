# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class SeiSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'SEI'
    lex = [('T_INSTRUCTION', 'SEI')]
    syn = ['S_IMPLIED']
    code = [0x78]
