# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class InySnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'INY'
    lex = [('T_INSTRUCTION', 'INY')]
    syn = ['S_IMPLIED']
    code = [0xc8]
