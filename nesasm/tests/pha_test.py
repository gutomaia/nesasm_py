# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class PhaSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'PHA'
    lex = [('T_INSTRUCTION', 'PHA')]
    syn = ['S_IMPLIED']
    code = [0x48]
