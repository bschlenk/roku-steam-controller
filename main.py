#!/usr/bin/env python

from settings import ROKU_IP
from roku import Roku
import sys
import argparse

roku = Roku(ROKU_IP)

def handle_args():
    parser = argparse.ArgumentParser(description='Press the given button on the roku remote.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('command', nargs='?', help='the command to run')
    group.add_argument('-c', '--commands', action='store_true', help='list the available commands')
    parser.add_argument('-r', '--repeat', metavar='n', type=int, default=1, help='repeat the command n times')
    return parser.parse_args()


def main():
    args = handle_args()
    if args.commands:
        print(*roku.commands, sep='\n')
        return

    command = getattr(roku, args.command)
    repeat = args.repeat

    for c in range(repeat):
        command()


main()
