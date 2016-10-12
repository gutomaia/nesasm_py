# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class TsxSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'TSX'
    lex = [('T_INSTRUCTION', 'TSX')]
    syn = ['S_IMPLIED']
    code = [0xba]
