# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class DeySnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'DEY'
    lex = [('T_INSTRUCTION', 'DEY')]
    syn = ['S_IMPLIED']
    code = [0x88]
