import unittest

from zope.component import queryUtility

from plone.app.redirector.tests.base import RedirectorTestCase
from plone.registry.interfaces import IRegistry

from collective.regexredirector.interfaces import IRegexRedirectionStorage,IRegexSettings

class TestRedirectorSetup(RedirectorTestCase):
    """Ensure that the basic regexredirector setup is successful.
    """
    def test_registry(self):
        registry= queryUtility(IRegistry)
        self.assertNotEquals(None, registry)
        settings = registry.forInterface(IRegexSettings)
        record_regex_values = registry.records['collective.regexredirector.interfaces.IRegexSettings.regex_values']
        self.failUnless('regex_values' in IRegexSettings)
        self.assertEquals(record_regex_values.value, u"")
    
    def test_utility(self):
        utility = queryUtility(IRegexRedirectionStorage)
        self.assertNotEquals(None, utility)

    def test_view(self):
        view = self.portal.restrictedTraverse('@@plone_redirector_view')
        self.assertNotEquals(None, view)        

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRedirectorSetup))
    return suite