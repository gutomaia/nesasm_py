# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class SecSnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'SEC'
    lex = [('T_INSTRUCTION', 'SEC')]
    syn = ['S_IMPLIED']
    code = [0x38]
