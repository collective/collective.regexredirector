from Products.PloneTestCase import ptc
from Products.PloneTestCase import layer

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
