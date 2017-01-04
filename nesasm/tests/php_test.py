# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class PhpSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'PHP'
    lex = [('T_INSTRUCTION', 'PHP')]
    syn = ['S_IMPLIED']
    code = [0x08]
