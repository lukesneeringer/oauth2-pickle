from __future__ import absolute_import
import pickle

from oauth2client.service_account import _ServiceAccountCredentials

from oauth2_test import utils


# Sanity check: It is easy to be confused about what environment you
# are in; if this is not being done with oauth2client 1.4.12, complain.
utils.expect_version('1.4.12')

# This private key is from the oauth2client 1.4.12 unit tests.
THROWAWAY_PRIVATE_KEY = """Bag Attributes
    friendlyName: key
    localKeyID: 22 7E 04 FC 64 48 20 83 1E C1 BD E3 F5 2F 44 7D EA 99 A5 BC
Key Attributes: <No Attributes>
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDh6PSnttDsv+vi
tUZTP1E3hVBah6PUGDWZhYgNiyW8quTWCmPvBmCR2YzuhUrY5+CtKP8UJOQico+p
oJHSAPsrzSr6YsGs3c9SQOslBmm9Fkh9/f/GZVTVZ6u5AsUmOcVvZ2q7Sz8Vj/aR
aIm0EJqRe9cQ5vvN9sg25rIv4xKwIZJ1VixKWJLmpCmDINqn7xvl+ldlUmSr3aGt
w21uSDuEJhQlzO3yf2FwJMkJ9SkCm9oVDXyl77OnKXj5bOQ/rojbyGeIxDJSUDWE
GKyRPuqKi6rSbwg6h2G/Z9qBJkqM5NNTbGRIFz/9/LdmmwvtaqCxlLtD7RVEryAp
+qTGDk5hAgMBAAECggEBAMYYfNDEYpf4A2SdCLne/9zrrfZ0kphdUkL48MDPj5vN
TzTRj6f9s5ixZ/+QKn3hdwbguCx13QbH5mocP0IjUhyqoFFHYAWxyyaZfpjM8tO4
QoEYxby3BpjLe62UXESUzChQSytJZFwIDXKcdIPNO3zvVzufEJcfG5no2b9cIvsG
Dy6J1FNILWxCtDIqBM+G1B1is9DhZnUDgn0iKzINiZmh1I1l7k/4tMnozVIKAfwo
f1kYjG/d2IzDM02mTeTElz3IKeNriaOIYTZgI26xLJxTkiFnBV4JOWFAZw15X+yR
+DrjGSIkTfhzbLa20Vt3AFM+LFK0ZoXT2dRnjbYPjQECgYEA+9XJFGwLcEX6pl1p
IwXAjXKJdju9DDn4lmHTW0Pbw25h1EXONwm/NPafwsWmPll9kW9IwsxUQVUyBC9a
c3Q7rF1e8ai/qqVFRIZof275MI82ciV2Mw8Hz7FPAUyoju5CvnjAEH4+irt1VE/7
SgdvQ1gDBQFegS69ijdz+cOhFxkCgYEA5aVoseMy/gIlsCvNPyw9+Jz/zBpKItX0
jGzdF7lhERRO2cursujKaoHntRckHcE3P/Z4K565bvVq+VaVG0T/BcBKPmPHrLmY
iuVXidltW7Jh9/RCVwb5+BvqlwlC470PEwhqoUatY/fPJ74srztrqJHvp1L29FT5
sdmlJW8YwokCgYAUa3dMgp5C0knKp5RY1KSSU5E11w4zKZgwiWob4lq1dAPWtHpO
GCo63yyBHImoUJVP75gUw4Cpc4EEudo5tlkIVuHV8nroGVKOhd9/Rb5K47Hke4kk
Brn5a0Ues9qPDF65Fw1ryPDFSwHufjXAAO5SpZZJF51UGDgiNvDedbBgMQKBgHSk
t7DjPhtW69234eCckD2fQS5ijBV1p2lMQmCygGM0dXiawvN02puOsCqDPoz+fxm2
DwPY80cw0M0k9UeMnBxHt25JMDrDan/iTbxu++T/jlNrdebOXFlxlI5y3c7fULDS
LZcNVzTXwhjlt7yp6d0NgzTyJw2ju9BiREfnTiRBAoGBAOPHrTOnPyjO+bVcCPTB
WGLsbBd77mVPGIuL0XGrvbVYPE8yIcNbZcthd8VXL/38Ygy8SIZh2ZqsrU1b5WFa
XUMLnGEODSS8x/GmW3i3KeirW5OxBNjfUzEF4XkJP8m41iTdsQEXQf9DdUY7X+CB
VL5h7N0VstYhGgycuPpcIUQa
-----END PRIVATE KEY-----
"""

# Create a _ServiceAccountCredentials object.
sac = _ServiceAccountCredentials(
    service_account_id='service-account-id',
    service_account_email='service@google.com',
    private_key_id='private-key-id',
    private_key_pkcs8_text=THROWAWAY_PRIVATE_KEY.encode('utf8'),
    scopes=['SCOPE1', 'SCOPE2', 'SCOPE3'],
    user_agent='user-agent/1.0',
)

# Write the pickle to disk.
with open('%s/service-acct-1.4.12.pickle' % utils.target, 'wb') as f:
    f.write(pickle.dumps(sac))
