# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class PlaSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'PLA'
    lex = [('T_INSTRUCTION', 'PLA')]
    syn = ['S_IMPLIED']
    code = [0x68]
