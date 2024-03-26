from nesasm import main
from nesasm.tests import FileTestCase
from unittest.mock import patch


class CommandLineTest(FileTestCase):

    @patch('nesasm.compile_file')
    def test_asm(self, compiler):
        main("nesasm asm fixtures/movingsprite/movingsprite.asm".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output=None, path=None)

    @patch('nesasm.compile_file')
    def test_asm_with_output(self, compiler):
        main("nesasm asm fixtures/movingsprite/movingsprite.asm --output"
             " /tmp/movingsprite.nes".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output='/tmp/movingsprite.nes', path=None)

    @patch('nesasm.compile_file')
    def test_asm_with_path(self, compiler):
        main("nesasm asm fixtures/movingsprite/movingsprite.asm --path "
             "fixtures/movingsprite".split())
        compiler.assert_called_once_with(
            'fixtures/movingsprite/movingsprite.asm',
            output=None, path='fixtures/movingsprite')
