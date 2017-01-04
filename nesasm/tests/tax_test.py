# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class TaxSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'TAX'
    lex = [('T_INSTRUCTION', 'TAX')]
    syn = ['S_IMPLIED']
    code = [0xaa]
