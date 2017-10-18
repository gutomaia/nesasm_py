# -*- coding: utf-8 -*-

from unittest import TestCase
from nesasm.compiler import compile
import os
import re

from nesasm.compiler import lexical, syntax, semantic


class MetaInstructionCase(type):

    def __new__(cls, name, bases, args):
        def gen_lex():
            def test(self):
                tokens = list(lexical(self.asm))
                self.assertEquals(len(tokens), len(self.lex))
                for i, l in enumerate(self.lex):
                    self.assertEquals(l[0], tokens[i]['type'])
                    self.assertEquals(l[1], tokens[i]['value'])
            return test

        def gen_syn():
            def test(self):
                tokens = [
                    {'type': l[0], 'value': l[1]}
                    for l in self.lex
                ]

                ast = syntax(tokens)
                self.assertEquals(len(ast), len(self.syn))
                for i, a in enumerate(self.syn):
                    self.assertEquals(ast[i]['type'], self.syn[i])
            return test

        def gen_sem():
            def test(self):
                ast = []

                token_counter = 0
                for i, a in enumerate(self.syn):
                    tokens = []
                    for j, l in enumerate(self.lex[token_counter:]):
                        if l[0] == 'T_ENDLINE':
                            token_counter = j + 1
                            break
                        tokens.append({'type': l[0], 'value': l[1]})

                    ast.append({'type': self.syn[i], 'children': tokens})

                # print ast
                compiled = semantic(ast)
                self.assertEquals(compiled, self.code)
            return test

        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        s3 = re.sub('_test$', '', s2)
        args['test_%s_lexical' % s3] = gen_lex()
        args['test_%s_syntax' % s3] = gen_syn()
        args['test_%s_semantic' % s3] = gen_sem()

        return type.__new__(cls, name, bases, args)


class FileTestCase(TestCase):

    def assertFileExists(self, filename):
        try:
            self.assertTrue(os.path.exists(filename))
        except AssertionError:
            raise AssertionError('File %s should exist' % filename)

    def assertFileNotExists(self, filename):
        try:
            self.assertFalse(os.path.exists(filename))
        except AssertionError:
            raise AssertionError('File %s should not exist' % filename)


class HexTestCase(TestCase):

    def assertHexEquals(self, expected, actual):
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        try:
            self.assertEquals(expected, actual)
        except AssertionError:
            line = 0
            cursor = 0
            lines = []
            out = ''
            while cursor < len(expected) or cursor < len(actual):
                for a in range(16):
                    if cursor < len(expected) and cursor < len(actual):
                        if expected[cursor] != actual[cursor] and line not in \
                                lines:
                            lines.append(line)
                    cursor += 1
                line += 1
            exp = ''
            act = ''
            for line in lines:
                exp = 'Expected: %04x: ' % (line)
                act = 'Actual  : %04x: ' % (line)
                for a in range(16):
                    cursor = (line * 16) + a
                    if cursor < len(expected) and cursor < len(actual):
                        if expected[cursor] != actual[cursor]:
                            exp += '%s%02x%s' % (
                                OKGREEN, ord(expected[cursor]), ENDC)
                            act += '%s%02x%s' % (
                                FAIL, ord(actual[cursor]), ENDC)
                        else:
                            exp += '%02x' % ord(expected[cursor])
                            act += '%02x' % ord(actual[cursor])
                    if ((a + 1) % 2) == 0:
                        exp += ' '
                        act += ' '
                out += '%s- %d \n' % (exp, line + 1)
                out += '%s- %d \n' % (act, line + 1)
            print(out)
            raise AssertionError('Hex are not equal')


class HexFileTestCase(HexTestCase):

    def assertHexFileEquals(self, expected, actual):
        with open(expected, 'rb') as f:
            expectedf = f.read()
        with open(actual, 'rb') as f:
            actualf = f.read()
        self.assertHexEquals(expectedf, actualf)
