# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase


class TaySnglTest(unittest.TestCase):
    __metaclass__ = MetaInstructionCase
    asm = 'TAY'
    lex = [('T_INSTRUCTION', 'TAY')]
    syn = ['S_IMPLIED']
    code = [0xa8]
