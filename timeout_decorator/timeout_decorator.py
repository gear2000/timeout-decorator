#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    :copyright: (c) 2012-2013 by PN.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import signal
import os

############################################################
# Timeout
############################################################

#http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/

class TimeoutError(Exception):
    def __init__(self, value = "Timed Out"):
        self.value = value
    def __str__(self):
        return repr(self.value)

#changed seconds_before_timeout to environmental variable

def timeout_env_var(var_timeout):
    def decorate(f):
        def handler(signum, frame):
            return 82
            #raise TimeoutError()
        def new_f(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            seconds_before_timeout = os.environ[var_timeout]
            signal.alarm(seconds_before_timeout)
            try:
                result = f(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old)
            signal.alarm(0)
            return result
        new_f.func_name = f.func_name
        return new_f
    return decorate

def timeout_secs(seconds_before_timeout):
    def decorate(f):
        def handler(signum, frame):
            return 82
            #raise TimeoutError()
        def new_f(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds_before_timeout)
            try:
                result = f(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old)
            signal.alarm(0)
            return result
        new_f.func_name = f.func_name
        return new_f
    return decorate
