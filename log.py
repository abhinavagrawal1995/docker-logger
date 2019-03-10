# Author: Abhinav Agrawal <abhinavagrawal1995@gmail.com
# This script executes the given commands and outputs the log according to the given options.
# Run this script with '-h' to see options.

#!/usr/bin/python
import sys
from subprocess import Popen, PIPE
import argparse
import logging



# Set the parser arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbosity', action='store_true', help='enable verbose logging')
parser.add_argument('--log-format', type=str, nargs = '*', help='Specify log format')
parser.add_argument('--log-date-format', type=str, nargs = '*', help='Specify date format')

def main():
	# Check if any options have been passed or if just the command has been passed.
	if len(inputs)>1:
		args, unknown = parser.parse_known_args(inputs[0].split(' '))
		index = 1
	else:
		args, unknown = parser.parse_known_args('')
		index = 0

	# Set date and log format
	if(getattr(args, 'log_format')):
		logFormat = ' '.join(getattr(args, 'log_format'))
	else:
		logFormat = "%(asctime)s *prefix* %(message)s"

	if(getattr(args, 'log_date_format')):
		dateFormat = ' '.join(getattr(args, 'log_date_format'))
	else:
		dateFormat = "%d/%m/%Y %I:%M:%S %p"

	logging.basicConfig(format=logFormat,datefmt=dateFormat)
	
	# Set log level depending on verbose flag 
	if(getattr(args, 'verbosity')):
		logging.getLogger().setLevel(logging.INFO)

	command =  inputs[index].split()
	logging.info("Going to run command: %s", command)

	#  Execute the command
	p = Popen(command, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()

	logging.info("Command exit code: " + str(p.returncode))

	if(len(stderr)>0):
		logging.warn("Produced %d bytes of stderr:",  len(stderr))
		for line in stderr.decode("utf-8").splitlines():
			logging.warn(line)

	if(len(stdout)>0):
		logging.info("Produced %d bytes of stdout:",  len(stdout))
		for line in stdout.decode("utf-8").splitlines():
			logging.info(line)



if __name__== "__main__":
	inputs = ' '.join(sys.argv[1:])
	inputs = inputs.split('-- ')
	index = 0
	main()