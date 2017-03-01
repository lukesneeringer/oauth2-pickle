from __future__ import absolute_import
import pickle
import sys


class OAuth2Unpickler(pickle.Unpickler):
    """Unpickler subclass that can unpickle alternate oauth2client paths.

    This subclass knows how to unpickle objects written by
    oauth2client_1_4_12_plus in oauth2client 4.0.0.

    It also knows how to unpickle objects written by oauth2client 1.4.12
    (either the original or the _plus variane) in oauth2client 4.0.0
    """
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

        # Run the base implementation.
        #
        # This is copied, rather than superclass-refereneced, so that
        # it will work on Python 2.
        __import__(module, level=0)
        return getattr(sys.modules[module], name)
