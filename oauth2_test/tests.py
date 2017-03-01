from __future__ import absolute_import
from datetime import datetime, timedelta
import os
import pickle
import platform
import sys
import unittest

import pkg_resources

from oauth2client.client import OAuth2Credentials
from oauth2client.service_account import ServiceAccountCredentials

from oauth2_test import utils


# Dump what version we are on, since keeping track might be more obnoxious
# than one expects.
print('These tests are running against Python {p}, oauth2client {o}'.format(
    o=pkg_resources.get_distribution('oauth2client').version,
    p=platform.python_version(),
))


class CredentialsReadTest(unittest.TestCase):
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
        with open('%s/credential-1.4.12.pickle' % utils.target, 'rb') as f:
            credential = pickle.loads(f.read())
        self._verify_credential(credential)

    def test_read_4_0_0_credentials(self):
        with open('%s/credential-4.0.0.pickle' % utils.target, 'rb') as f:
            credential = pickle.loads(f.read())
        self._verify_credential(credential)


class ServiceAccountRestTest(unittest.TestCase):
    def _verify_sac(self, sac):
        self.assertIsInstance(sac, ServiceAccountCredentials)
        self.assertEqual(sac._service_account_email, 'service@google.com')
        self.assertEqual(sac._private_key_id, 'private-key-id')
        self.assertEqual(sac._scopes, 'SCOPE1 SCOPE2 SCOPE3')
        self.assertEqual(sac.client_id, None)
        self.assertEqual(sac._user_agent, 'user-agent/1.0')
        self.assertEqual(sac._kwargs, {})

    def test_read_1_4_12_sac(self):
        with open('%s/service-acct-1.4.12.pickle' % utils.target, 'rb') as f:
            sac = pickle.loads(f.read())
        self._verify_sac(sac)

    def test_read_4_0_0_sac(self):
        with open('%s/service-acct-4.0.0.pickle' % utils.target, 'rb') as f:
            sac = pickle.loads(f.read())
        self._verify_sac(sac)
