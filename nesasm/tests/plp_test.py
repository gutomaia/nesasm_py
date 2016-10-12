# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class PlpSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'PLP'
    lex = [('T_INSTRUCTION', 'PLP')]
    syn = ['S_IMPLIED']
    code = [0x28]
