# -*- coding: utf-8 -*-
import unittest
from nesasm.tests import MetaInstructionCase
from six import add_metaclass


@add_metaclass(MetaInstructionCase)
class ClvImplTest(unittest.TestCase):

    asm = 'CLV'
    lex = [('T_INSTRUCTION', 'CLV')]
    syn = ['S_IMPLIED']
    code = [0xb8]
