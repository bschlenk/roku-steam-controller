#!/usr/bin/env python

from settings import ROKU_IP
from roku import Roku
import sys

roku = Roku(ROKU_IP)

if len(sys.argv) != 2:
    print('usage: {} <command>'.format(sys.argv[0]))
    sys.exit(1)

command = sys.argv[1]
getattr(roku, command)()

