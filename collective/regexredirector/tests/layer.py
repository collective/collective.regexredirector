from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import ptc
from Products.PloneTestCase import layer
from Products.Five import zcml
from Products.Five import fiveconfigure

ptc.setupPloneSite(
    extension_profiles=('collective.regexredirector:default', )
)

class RegexRedirectionLayer(layer.PloneSite):
    """Configure collective.akismet"""

    @classmethod
    def setUp(cls):
		pass

    @classmethod
    def tearDown(cls):
        pass
