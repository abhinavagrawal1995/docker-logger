#!/usr/bin/python
import sys
from subprocess import Popen, PIPE
import argparse

# cmd = sys.argv[1]
# args = cmd.parse_args()
# p = Popen(cmd, stdout=PIPE, stderr=PIPE)
# stdout, stderr = p.communicate()
parser = argparse.ArgumentParser(usage="<entry-point-options> -- <command> [command-args...]")
parser.add_argument('command', action="store", help="The command to run", nargs='*')
parser.add_argument('-v', '--verbosity', action="store_true", help="enable verbose logging")
parser.add_argument('--log-format', action="store", help="enable verbose logging")
args = parser.parse_args()
print(args)	
# print("stdout" + stdout)	
# print("stderr" + stderr)
