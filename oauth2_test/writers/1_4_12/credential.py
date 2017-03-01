from __future__ import absolute_import
from datetime import datetime, timedelta
import os
import pickle
import sys

import pkg_resources

from oauth2client.client import OAuth2Credentials


# Sanity check: It is easy to be confused about what environment you
# are in; if this is not being done with oauth2client 1.4.12, complain.
if pkg_resources.get_distribution('oauth2client').version != '1.4.12':
    raise RuntimeError('Run this with oauth2client 1.4.12')

# These are copied from `test_file.py` in oauth2client 1.4.12.
access_token = 'foo'
client_id = 'some-client-id'
client_secret = 'cOuDdkfjxxnv+'
refresh_token = '1/0/a.df219fjls0'
token_expiry = datetime.utcnow() + timedelta(days=7)
token_uri = 'https://www.google.com/accounts/o8/oauth2/token'
user_agent = 'refresh_checker/1.0'

# Create a credential, pickle it, and write it to a file.
credentials = OAuth2Credentials(
    access_token, client_id, client_secret,
    refresh_token, token_expiry, token_uri, user_agent,
)

# Serialize the credentials and write them to a file.
serialized = pickle.dumps(credentials)
target = os.environ['OAUTH2_TEST_DATA']
with open('%s/credential-1.4.12.pickle' % target, 'wb') as f:
    f.write(serialized)
