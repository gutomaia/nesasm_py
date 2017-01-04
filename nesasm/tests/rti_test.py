# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class RtiSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'RTI'
    lex = [('T_INSTRUCTION', 'RTI')]
    syn = ['S_IMPLIED']
    code = [0x40]
