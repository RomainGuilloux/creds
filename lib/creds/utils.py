# -*- coding: utf-8 -*-
""" Some docstring. """

from __future__ import (unicode_literals, print_function)

import base64
import os
import platform
import random
import string
import subprocess

from creds.constants import SUPPORTED_PLATFORMS
from external.six import (PY2, PY3)


def sudo_check():
    """ Return the string 'sudo' if current user isn't root. """
    if os.geteuid() != 0:
        return 'sudo'
    else:
        return ''


def check_platform():
    """ Return an error if this is being used on unsupported platform. """
    if not platform.system() in SUPPORTED_PLATFORMS:
        raise OSError('Linux is currently the only supported platform for this library.')


def execute_command(command=None):
    """ Execute a command and return the stdout and stderr. """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.communicate()


def random_string(length=None):
    """ Some doc string. """
    if not length:
        length = 10
    """ Generate a random string of ASCII characters. """
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


def base64encode(_input=None):
    """ Return base64 encoded representation of a string. """
    #if PY2:
    # return base64.b64encode(_input)
    #elif PY3:
    if isinstance(_input, bytes):
        return base64.b64encode(_input).decode('UTF-8')
    elif isinstance(_input, str):
        return base64.b64encode(bytearray(_input, encoding='UTF-8')).decode('UTF-8')


def base64decode(_input=None):
    """ Take a base64 encoded string and return the decoded string. """
    missing_padding = 4 - len(_input) % 4
    if missing_padding:
        _input += '=' * missing_padding
    if PY2:
        return base64.decodestring(_input)
    elif PY3:
        if isinstance(_input, bytes):
            return base64.b64decode(_input).decode('UTF-8')
        elif isinstance(_input, str):
            return base64.b64decode(bytearray(_input, encoding='UTF-8')).decode('UTF-8')
