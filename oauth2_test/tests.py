from __future__ import absolute_import
from datetime import datetime, timedelta
import os
import pickle
import platform
import sys
import unittest

import pkg_resources

import pytz

import six

from oauth2client.client import OAuth2Credentials
from oauth2client.service_account import ServiceAccountCredentials

from oauth2_test import serializers
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
        self.assertEqual(credential.token_expiry.year, 2012)
        self.assertEqual(credential.token_expiry.month, 4)
        self.assertEqual(credential.token_expiry.day, 21)
        self.assertEqual(credential.token_expiry.tzinfo, pytz.UTC)
        self.assertIn('google.com', credential.token_uri)
        self.assertEqual(credential.user_agent, 'refresh_checker/1.0')

    def test_read_1_4_12_py27_credentials(self):
        filename = '%s/credential-1.4.12-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            credential = serializers.OAuth2Unpickler(f).load()
        self._verify_credential(credential)

    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_1_4_12_py36_credentials(self):
        filename = '%s/credential-1.4.12-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            credential = pickle.load(f)
        self._verify_credential(credential)

    def test_read_4_0_0_py27_credentials(self):
        filename = '%s/credential-4.0.0-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            credential = serializers.OAuth2Unpickler(f).load()
        self._verify_credential(credential)

    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_4_0_0_py36_credentials(self):
        filename = '%s/credential-4.0.0-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            credential = pickle.load(f)
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

    @unittest.expectedFailure
    def test_read_1_4_12_py27_sac_without_custom_unpickler(self):
        filename = '%s/service-acct-1.4.12-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = pickle.loads(f.read())
        self._verify_sac(sac)

    @unittest.expectedFailure
    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_1_4_12_py36_sac_without_custom_unpickler(self):
        filename = '%s/service-acct-1.4.12-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = pickle.load(f)
        self._verify_sac(sac)

    def test_read_1_4_12_py27_sac_with_custom_unpickler(self):
        filename = '%s/service-acct-1.4.12-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = serializers.OAuth2Unpickler(f).load()
        self._verify_sac(sac)

    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_1_4_12_py36_sac_with_custom_unpickler(self):
        filename = '%s/service-acct-1.4.12-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = serializers.OAuth2Unpickler(f).load()
        self._verify_sac(sac)

    def test_read_4_0_0_py27_sac_without_custom_unpickler(self):
        filename = '%s/service-acct-4.0.0-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = pickle.load(f)
        self._verify_sac(sac)

    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_4_0_0_py36_sac_without_custom_unpickler(self):
        filename = '%s/service-acct-4.0.0-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = pickle.load(f)
        self._verify_sac(sac)

    def test_read_4_0_0_py27_sac_with_custom_unpickler(self):
        filename = '%s/service-acct-4.0.0-py27.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = serializers.OAuth2Unpickler(f).load()
        self._verify_sac(sac)

    @unittest.skipIf(six.PY2, 'Python 2 only reads Python 2 pickles.')
    def test_read_4_0_0_py36_sac_with_custom_unpickler(self):
        filename = '%s/service-acct-4.0.0-py36.pickle' % utils.target
        with open(filename, 'rb') as f:
            sac = serializers.OAuth2Unpickler(f).load()
        self._verify_sac(sac)
