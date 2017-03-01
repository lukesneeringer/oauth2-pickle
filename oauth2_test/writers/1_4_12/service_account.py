from __future__ import absolute_import
import pickle

from oauth2client.service_account import _ServiceAccountCredentials

from oauth2_test import utils


# Sanity check: It is easy to be confused about what environment you
# are in; if this is not being done with oauth2client 1.4.12, complain.
utils.expect_version('1.4.12')

# Create a _ServiceAccountCredentials object.
sac = _ServiceAccountCredentials(
    service_account_id='service-account-id',
    service_account_email='service@google.com',
    private_key_id='private-key-id',
    private_key_pkcs8_text='private-key==',
    scopes=['SCOPE1', 'SCOPE2', 'SCOPE3'],
    user_agent='user-agent/1.0',
)

# Write the pickle to disk.
with open('%s/service-acct-1.4.12.pickle' % utils.target, 'wb') as f:
    f.write(pickle.dumps(sac))
