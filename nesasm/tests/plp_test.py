# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class PlpSnglTest(unittest.TestCase):
    asm = 'PLP'
    lex = [('T_INSTRUCTION', 'PLP')]
    syn = ['S_IMPLIED']
    code = [0x28]
