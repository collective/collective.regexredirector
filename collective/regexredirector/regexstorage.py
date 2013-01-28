from plone.app.redirector.storage import RedirectionStorage
from plone.app.redirector.interfaces import IRedirectionStorage
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.regexredirector.interfaces import *
from collective.regexredirector.utils import parse_to_array
from zope.interface import implements
import re

class RegexRedirectionStorage(RedirectionStorage):

    implements(IRedirectionStorage)

    def has_path(self, old_path,settings=None):
		found=super(RegexRedirectionStorage, self).has_path(old_path)
		if found!=True:
				if settings==None:
					settings=self.get_regex_registry()
				regex_array = parse_to_array(settings.regex_values.__str__())
				for regex in regex_array.keys():
					url_re=re.match(regex, old_path)
					if url_re:
						found=True
						break
		return found 
		
    def get(self,old_path,default=None):
		result=super(RegexRedirectionStorage, self).get(old_path,default)
		if result is None:
			settings=self.get_regex_registry()
			regex_array = parse_to_array(settings.regex_values.__str__())
			for regex in regex_array.keys():
				url_re=re.match(regex, old_path)
				if url_re:
					return re.sub(regex,regex_array[regex],old_path)
		return result
		
	def get_regex_registry():
		registry = getUtility(IRegistry)
		settings = registry.forInterface(IRegexSettings)
		return settings
