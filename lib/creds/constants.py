# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function)

import os
import io

from external.six.six import text_type, PY2, PY3

SUPPORTED_PLATFORMS = ['Linux']

PURGE_UNDEFINED = False  # Purge any users that fall between UID_MIN and UID_MAX that are not defined

DEFAULT_UID_MIN = 1000  # The lowest uid to consider safe to manage
DEFAULT_UID_MAX = 60000  # The maximum uid to consider safe to manage


def login_defs():

    uid_min = None
    uid_max = None
    login_defs_path = '/etc/login.defs'
    if os.path.exists(login_defs_path):
        with io.open(text_type(login_defs_path), encoding=text_type('utf-8')) as log_defs_file:
            login_data = log_defs_file.readlines()
        for line in login_data:
            if PY3:
                line = str(line)
            if PY2:
                line = line.encode(text_type('utf8'))
            if line[:6] == text_type('UID_MIN'):
                uid_min = int(line.split()[1].strip())
            if line[:6] == text_type('UID_MAX'):
                uid_max = int(line.split()[1].strip())
    if not uid_min:
        uid_min = DEFAULT_UID_MIN
    if not uid_max:
        uid_max = DEFAULT_UID_MAX
    return uid_min, uid_max


UID_MIN, UID_MAX = login_defs()
ALLOW_NON_UNIQUE_ID = False  # Allow multiple users to share uids
PROTECTED_USERS = list()  # Users that must not be affected
