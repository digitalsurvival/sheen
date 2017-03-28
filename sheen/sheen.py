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
__author__ = u'matthew marchese'
__email__ = 'maffblaster@gentoo.org'
__description__ = 'a cross-platform desktop screenshot boasting tool'
__source__ = 'https://github.com/digitalsurvival/sheen'
__package__ = 'sheen'

import platform # Get system information
import socket # Get IP addresses
import getpass # Get username
from os import getenv

from docopt import docopt # CLI

def show_platform():
    print(getpass.getuser() + '@' + platform.node())
    print('OS: ' + str(platform.system()))
    print('Kernel: ' + platform.machine() + ' ' + platform.release())
    #print('Uptime: ')
    # print('Packages: ')
    print('Shell: ' + getenv('SHELL'))
    print('IPv4: ' + socket.gethostbyname(socket.gethostname()))

    print('CPU: ' + platform.processor())
    # print('RAM: ')

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)

    if arguments['--debug'] == True:
        print('Passed arguments:\n' + arguments)

    show_platform()