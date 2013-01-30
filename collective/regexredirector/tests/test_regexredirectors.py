import unittest, transaction

from zope.component import getUtility, queryUtility

from plone.registry.interfaces import IRegistry

from collective.regexredirector.interfaces import IRegexSettings
from collective.regexredirector.interfaces import IRegexRedirectionStorage
from collective.regexredirector.tests import layer
from collective.regexredirector.tests.base import RedirectorTestCase

class RegistryTest(RedirectorTestCase):
	"""
		In Developppement.... Doesn't work...
	"""
	layer = layer.RegexRedirectionLayer

	def afterSetUp(self):
		self.loginAsPortalOwner()
		self.storage = queryUtility(IRegexRedirectionStorage)
		self.registry= getUtility(IRegistry)
		self.settings = self.registry.forInterface(IRegexSettings)

	def test_regexredirector_addregistry(self):
		stri="'/tags/(?P<category_name>.+)'='/category/\g<category_name>/view'\r\n'/references/(?P<category_name>.+)'='/realisations/\g<category_name>'"
		self.assertNotEquals(self.settings,None)
		self.assertEquals(self.settings.regex_values,"")
		self.settings.regex_values=unicode(stri)
		transaction.commit()

		
	def test_regexredirector_storage_haspath(self):
		has_path1=self.storage.has_path("/tags/toto")
		self.assertEquals(has_path1, True)
		has_path2=self.storage.has_path("/references/toto")
		self.assertEquals(has_path2, True)
		
	def test_regexredirector_storage_get(self):
		get_path=self.storage.get("/tags/toto")
		self.assertEquals(get_path,"/category/toto/view")

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
