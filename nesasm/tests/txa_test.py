# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class TxaSnglTest(unittest.TestCase):
    asm = 'TXA'
    lex = [('T_INSTRUCTION', 'TXA')]
    syn = ['S_IMPLIED']
    code = [0x8a]
