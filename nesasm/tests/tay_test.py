# -*- coding: utf-8 -*-

import unittest

from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class TaySnglTest(unittest.TestCase):
    asm = 'TAY'
    lex = [('T_INSTRUCTION', 'TAY')]
    syn = ['S_IMPLIED']
    code = [0xa8]
