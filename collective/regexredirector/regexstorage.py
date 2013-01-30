from plone.app.redirector.storage import RedirectionStorage
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implements
from interfaces import IRegexSettings,IRegexRedirectionStorage
import re

class RegexRedirectionStorage(RedirectionStorage):
    implements(IRegexRedirectionStorage)

    def has_path(self, old_path,settings=None):
		"""
		After watching on superclass, look on regex registry if the oldpath is redirected
		"""
		found=super(RegexRedirectionStorage, self).has_path(old_path)
		if found!=True:
				if settings==None:
					settings=self.get_regex_registry()
				regex_array = self.parse_to_array(settings.regex_values.__str__())
				for regex in regex_array.keys():
					url_re=re.match(regex, old_path)
					if url_re:
						found=True
						break
		return found 
		
    def get(self,old_path,default=None):
		"""
		After watching on superclass, look on regex registry if the oldpath is redirected and 
		return the new url in paying attention on the regex pattern
		"""
		result=super(RegexRedirectionStorage, self).get(old_path,default)
		if result is None:
			settings=self.get_regex_registry()
			regex_array = self.parse_to_array(settings.regex_values.__str__())
			for regex in regex_array.keys():
				url_re=re.match(regex, old_path)
				if url_re:
					return re.sub(regex,regex_array[regex],old_path)
		return result

    def get_regex_registry(self):
		registry = getUtility(IRegistry)
		settings = registry.forInterface(IRegexSettings)
		return settings

    def parse_to_array(self,regex_string):
        result={}
        retur=regex_string.split("\r\n")
        for element in retur:
            element2=element.split("=")
            if len(element2)>1:
                result[element2[0].replace("'","")]=element2[1].replace("'","")
        return result