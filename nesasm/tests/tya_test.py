# -*- coding: utf-8 -*-
import unittest

from nesasm.tests import MetaInstructionCase


class TyaSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'TYA'
    lex = [('T_INSTRUCTION', 'TYA')]
    syn = ['S_IMPLIED']
    code = [0x98]
