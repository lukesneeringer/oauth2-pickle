from __future__ import absolute_import
from datetime import datetime, timedelta
import os
import pickle
import platform
import sys
import unittest

import pkg_resources

from oauth2client.client import OAuth2Credentials


# Dump what version we are on, since keeping track might be more obnoxious
# than one expects.
print('These tests are running against Python {p}, oauth2client {o}'.format(
    o=pkg_resources.get_distribution('oauth2client').version,
    p=platform.python_version(),
))


class CredentialsReadTest(unittest.TestCase):
    data_dir = os.environ['OAUTH2_TEST_DATA']
    
    def _verify_credential(self, credential):
        self.assertIsInstance(credential, OAuth2Credentials)
        self.assertEqual(credential.access_token, 'foo')
        self.assertEqual(credential.client_id, 'some-client-id')
        self.assertEqual(credential.client_secret, 'cOuDdkfjxxnv+')
        self.assertEqual(credential.refresh_token, '1/0/a.df219fjls0')
        self.assertIsInstance(credential.token_expiry, datetime)
        self.assertIn('google.com', credential.token_uri)
        self.assertEqual(credential.user_agent, 'refresh_checker/1.0')

    def test_read_1_4_12_credentials(self):
        with open('%s/credential-1.4.12.pickle' % self.data_dir, 'rb') as f:
            credential = pickle.loads(f.read())
        self._verify_credential(credential)

    def test_read_4_0_0_credentials(self):
        with open('%s/credential-4.0.0.pickle' % self.data_dir, 'rb') as f:
            credential = pickle.loads(f.read())
        self._verify_credential(credential)
