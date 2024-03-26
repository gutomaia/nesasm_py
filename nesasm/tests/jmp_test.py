# -*- coding: utf-8 -*-

import unittest

from nesasm.compiler import lexical, syntax, semantic


class JmpTest(unittest.TestCase):

    def test_jmp_abs(self):
        tokens = list(lexical('JMP $1234'))
        self.assertEqual(2, len(tokens))
        self.assertEqual('T_INSTRUCTION', tokens[0]['type'])
        self.assertEqual('T_ADDRESS', tokens[1]['type'])
        self.assertEqual('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEqual(1, len(ast))
        self.assertEqual('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEqual(code, [0x4c, 0x34, 0x12])

# TODO: http://www.6502.buss.hk/6502-instruction-set/jmp says that there
# is a indirect
