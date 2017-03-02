from __future__ import absolute_import
import pickle
import sys

from oauth2client.service_account import ServiceAccountCredentials

from oauth2_test import utils


# Sanity check: It is easy to be confused about what environment you
# are in; if this is not being done with oauth2client 4.0.0, complain.
utils.expect_version('4.0.0')

# Create a _ServiceAccountCredentials object.
sac = ServiceAccountCredentials(
    service_account_email='service@google.com',
    signer=None,
    scopes=['SCOPE1', 'SCOPE2', 'SCOPE3'],
    private_key_id='private-key-id',
    user_agent='user-agent/1.0',
)

# Write the pickle to disk.
filename = '{target}/service-acct-4.0.0-py{py_major}{py_minor}.pickle'.format(
    py_major=sys.version_info[0],
    py_minor=sys.version_info[1],
    target=utils.target,
)
with open(filename, 'wb') as f:
    f.write(pickle.dumps(sac))
