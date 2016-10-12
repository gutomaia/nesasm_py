# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class TxaSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'TXA'
    lex = [('T_INSTRUCTION', 'TXA')]
    syn = ['S_IMPLIED']
    code = [0x8a]
