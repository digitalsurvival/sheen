#!/usr/bin/env python3

"""Usage:
  sheen [--debug] [-V | --verbose]
  sheen [-h | --help] | [--version]

Options:
  -h --help            show this help message and exit
  --version            show version and exit
  -v --verbose         show extended information
  --debug              enable debugging output (stdout)
"""

__version__ = '0.0.1'
__package__ = 'sheen'
__status__ = 'alpha'
__license__ = 'MIT'
__author__ = u'matthew marchese'
__email__ = 'maffblaster@gentoo.org'
__maintainer__ = u'matthew marchese'
__contributors__ = ''
__copyright__ = '2017'
__description__ = 'a cross-platform desktop screenshot boasting tool'
__url__ = 'https://github.com/digitalsurvival/sheen'
__source__ = 'https://github.com/digitalsurvival/sheen'

import platform # Get system information
import socket # Get IP addresses
import getpass # Get (current) username
import sys
import logging

import datetime
from os import getenv # Specific user environment values

from docopt import docopt

logger = logging.basicConfig(filename=__package__ + '.log',level=logging.INFO)

# Python 3 validator
if sys.version_info < (3, 0):
    print(__name__ + " requires Python 3.0 and up. Exiting...\n")
    sys.exit(1)

def get_uptime(system):
    """Returns a human-readable string based on system"""

    if system == 'Linux':
        with open('/proc/uptime', 'r') as f:  # First number is uptime in seconds
            output = f.readline().split(' ')  # Only read the first line; file should never be bigger
            seconds = round(float(output[0]))
            uptime = datetime.datetime(second=seconds)
            print(str(seconds) + 's')
            minuets = seconds / 60
            hours = minuets / 60
            days = hours / 24
            years = days / 356

            uptime = str(years) + 'y ' + str(days) + 'd ' + str(hours) + 'h ' + str(minuets) + 'm '
    else:
        uptime = 'Unknown...'

    return uptime

def show_platform():
    logging.debug('')
    print(getpass.getuser() + '@' + platform.node())
    print('OS: ' + str(platform.system()))
    print('Kernel: ' + platform.machine() + ' ' + platform.system() + ' ' + platform.release())
    print('Uptime: ' + get_uptime(platform.system()))
    # print('Packages: ')
    print('Shell: ' + getenv('SHELL'))
    print('IPv4: ' + socket.gethostbyname(socket.gethostname()))

    print('CPU: ' + platform.processor())
    # print('RAM: ')

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)

    

    show_platform()
