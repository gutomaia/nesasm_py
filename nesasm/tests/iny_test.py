# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class InySnglTest(unittest.TestCase):
    asm = 'INY'
    lex = [('T_INSTRUCTION', 'INY')]
    syn = ['S_IMPLIED']
    code = [0xc8]
