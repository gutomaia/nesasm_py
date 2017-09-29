# -*- coding: utf-8 -*-
import unittest

from nesasm.compiler import lexical, syntax, semantic


class ConstantsTest(unittest.TestCase):

    def test_constant(self):
        tokens = list(lexical('FOO = #$10'))

        self.assertEquals(3, len(tokens))
        self.assertEquals('T_MARKER', tokens[0]['type'])
        self.assertEquals('T_EQUAL', tokens[1]['type'])
        self.assertEquals('T_HEX_NUMBER', tokens[2]['type'])

        ast = syntax(tokens)

        code = semantic(ast)
        self.assertEquals(code, [])

