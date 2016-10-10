# -*- coding: utf-8 -*-
from __future__ import absolute_import

import argparse
from nesasm.compiler import compile_file

def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="nesasm",
        description='NESasm - NES Assembly Compiler',
        epilog='')

    subparsers = parser.add_subparsers(
        title="subcommands", description="utilities", help="aditional help")


    asm_cmd = subparsers.add_parser('asm')  # TODO, aliases=['asm'])
    asm_cmd.add_argument('input', nargs='?', metavar='INPUT',
                         help="input c6502 asm file")
    asm_cmd.add_argument('-o', '--output', metavar='OUTPUT',
                         help="output NES file")
    asm_cmd.add_argument('-p', '--path', metavar='PATH',
                         help="path for assets")
    asm_cmd.set_defaults(func=exec_asm)


    args = parser.parse_args(argv[1:])
    args.func(args)

def exec_asm(args):
    compile_file(args.input, output=args.output, path=args.path)
