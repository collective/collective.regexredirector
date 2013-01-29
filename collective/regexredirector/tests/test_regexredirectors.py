import unittest

from zope.component import getMultiAdapter

from plone.registry import Registry
import transaction

from collective.regexredirector.interfaces import IRegexSettings
from collective.regexredirector.regexstorage import RegexRedirectionStorage
from plone.app.redirector.interfaces import IRedirectionStorage, IFourOhFourView
from collective.regexredirector.tests import layer
from collective.regexredirector.tests.base import RedirectorTestCase
from zope.component import getUtility, queryUtility
from plone.registry.interfaces import IRegistry

class RegistryTest(RedirectorTestCase):
	"""
		In Developppement.... Doesn't work...
	"""
	layer = layer.RegexRedirectionLayer

	def afterSetUp(self):
		self.loginAsPortalOwner()
		#self.storage = queryUtility(IRedirectionStorage)
		self.storage = queryUtility(IFourOhFourView)
		self.registry= getUtility(IRegistry)
		self.settings = self.registry.forInterface(IRegexSettings)
		#self.portal.invokeFactory('Folder', 'testfolder')
		#print(self.portal)
        #self.folder = self.portal.testfolder
	
	def test(self):
		print self.storage
	#def test_regexredirector_addregistry(self):
	#	stri="'/tags/(?P<category_name>.+)'='/category/\g<category_name>/view'\r\n'/references/(?P<category_name>.+)'='/realisations/\g<category_name>'"
	#	self.settings.regex_values=unicode(stri)
	#	transaction.commit()
	#	print(" setRegistry => "+self.settings.regex_values)
		
	#def test_regexredirector_haspath(self):
	#	print(" /tags/toto => "+self.storage.has_path("/tags/toto").__str__())
	#	print(" references/toto => "+self.storage.has_path("/references/toto").__str__())
		
	#def test_regexredirector_get(self):
	#	print(" /tags/toto => "+self.storage.get("/tags/toto").__str__())

		
"""def test_regexredirector_controlpanel_view(self):
	view = getMultiAdapter((self.portal, self.portal.REQUEST), 
						   name="regexredirector-settings")
	view = view.__of__(self.portal)
	self.failUnless(view())
"""
def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
