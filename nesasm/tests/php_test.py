# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class PhpSnglTest(unittest.TestCase):
    asm = 'PHP'
    lex = [('T_INSTRUCTION', 'PHP')]
    syn = ['S_IMPLIED']
    code = [0x08]
