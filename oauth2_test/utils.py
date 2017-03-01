from __future__ import absolute_import
import os

import pkg_resources


oauth2client_version = pkg_resources.get_distribution('oauth2client').version

def expect_version(expected):
    if oauth2client_version != expected:
        raise RuntimeError('Run this with oauth2client %s.' % expected)


target = os.environ['OAUTH2_TEST_DATA']
