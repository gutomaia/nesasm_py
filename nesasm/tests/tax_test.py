# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class TaxSnglTest(unittest.TestCase):
    asm = 'TAX'
    lex = [('T_INSTRUCTION', 'TAX')]
    syn = ['S_IMPLIED']
    code = [0xaa]
