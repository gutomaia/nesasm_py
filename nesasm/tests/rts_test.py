# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class RtsSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'RTS'
    lex = [('T_INSTRUCTION', 'RTS')]
    syn = ['S_IMPLIED']
    code = [0x60]
