import unittest
from plone.app.redirector.tests.base import RedirectorTestCase

from zope.component import queryUtility
from collective.regexredirector.interfaces import IRegexRedirectionStorage,\
    IRegexSettings
from plone.registry.interfaces import IRegistry
class TestRedirectorSetup(RedirectorTestCase):
    """Ensure that the basic regexredirector setup is successful.
    """
    def test_registry(self):
        registry= queryUtility(IRegistry)
        self.assertNotEquals(None, registry)
        settings = registry.forInterface(IRegexSettings)
        print registry
        record_regex_values = registry.records['collective.regexredirector.interfaces.IRegexSettings.regex_values']
        print settings
        self.failUnless('regex_values' in IRegexSettings)
        self.assertEquals(record_regex_values.value, u"")
    
    def test_utility(self):
        utility = queryUtility(IRegexRedirectionStorage)
        print utility
        self.assertNotEquals(None, utility)

    def test_view(self):
        view = self.portal.restrictedTraverse('@@plone_redirector_view')
        print view
        self.assertNotEquals(None, view)
        

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRedirectorSetup))
    return suite