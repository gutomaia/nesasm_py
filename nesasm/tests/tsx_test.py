# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class TsxSnglTest(unittest.TestCase):
    asm = 'TSX'
    lex = [('T_INSTRUCTION', 'TSX')]
    syn = ['S_IMPLIED']
    code = [0xba]
