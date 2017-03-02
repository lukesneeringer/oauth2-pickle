from __future__ import absolute_import
import pickle
import sys

import six


# Subclass from pickle._Unpickler on Python 3, and pickle.Unpickler on 2.7.
#
# This ensures that we always get the pure Python implementation, and never
# the C implementation. Since we are using private API in order to do this,
# it matters that we know which one we are dealing with.
Unpickler = getattr(pickle, '_Unpickler', pickle.Unpickler)


class OAuth2Unpickler(Unpickler):
    """Unpickler subclass that can unpickle alternate oauth2client paths.

    This subclass knows how to unpickle objects written by
    oauth2client_1_4_12_plus in oauth2client 4.0.0.

    It also knows how to unpickle objects written by oauth2client 1.4.12
    (either the original or the _plus variane) in oauth2client 4.0.0
    """
    def _decode_string(self, value):
        """Gracefully attempt to decode the value as ASCII.

        Try to decode the value as ASCII, but return the bytes object
        as-is if decoding fails.

        This makes Python 2 datetime pickles correctly deserialize under
        Python 3.
        """
        try:
            return value.decode(self.encoding, self.errors)
        except UnicodeDecodeError:
            return value

    def load_global(self):
        """Run the Python 3 `load_global` implementation.

        This makes `find_class` work, even on Python 2.
        """
        module = self.readline()[:-1].decode('utf8')
        name = self.readline()[:-1].decode('utf8')
        class_ = self.find_class(module, name)
        self.append(class_)

    def find_class(self, module, name):
        """Return the appropriate class.

        Rewrite oauth2client_1_4_12_plus paths to the regular client,
        and handle other rewrites vaused by oauth2client version upgrades.
        """
        # If the module contains "oauth2client_1_4_12_plus", rewrite it
        # to just oauth2client.
        module = module.replace('oauth2client_1_4_12_plus', 'oauth2client')

        # If the name contains "_ServiceAccountCredentials", rewrite it
        # to "ServiceAccountCredentials"
        name = name.replace('_ServiceAccountCredentials',
                            'ServiceAccountCredentials')

        # Run a modified version of the base implementation.
        #
        # This is required in its modified form to work correctly on both
        # Python 2 and Python 3.
        if six.PY3:
            import _compat_pickle
            if (module, name) in _compat_pickle.NAME_MAPPING:
                module, name = _compat_pickle.NAME_MAPPING[(module, name)]
            elif module in _compat_pickle.IMPORT_MAPPING:
                module = _compat_pickle.IMPORT_MAPPING[module]
        __import__(module, level=0)
        return getattr(sys.modules[module], name)
