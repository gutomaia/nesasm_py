# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class SedSnglTest(unittest.TestCase):
    asm = 'SED'
    lex = [('T_INSTRUCTION', 'SED')]
    syn = ['S_IMPLIED']
    code = [0xf8]
