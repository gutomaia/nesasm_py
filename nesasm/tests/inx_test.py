# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class InxSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'INX'
    lex = [('T_INSTRUCTION', 'INX')]
    syn = ['S_IMPLIED']
    code = [0xe8]
