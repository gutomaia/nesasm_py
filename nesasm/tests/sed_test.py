# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class SedSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'SED'
    lex = [('T_INSTRUCTION', 'SED')]
    syn = ['S_IMPLIED']
    code = [0xf8]
