# -*- coding: utf-8 -*-
from pynes import main
from pynes.tests import FileTestCase
from mock import patch


class CommandLineTest(FileTestCase):

    @patch('pynes.compiler.compile_file')
    def test_asm(self, compiler):
        main("pynes asm fixtures/movingsprite/movingsprite.asm".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output=None, path=None)

    @patch('pynes.compiler.compile_file')
    def test_asm_with_output(self, compiler):
        main("pynes asm fixtures/movingsprite/movingsprite.asm --output"
             " /tmp/movingsprite.nes".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output='/tmp/movingsprite.nes', path=None)

    @patch('pynes.compiler.compile_file')
    def test_asm_with_path(self, compiler):
        main("pynes asm fixtures/movingsprite/movingsprite.asm --path "
             "fixtures/movingsprite".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output=None, path='fixtures/movingsprite')
