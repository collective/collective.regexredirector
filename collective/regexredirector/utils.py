from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.regexredirector.interfaces import IRegexSettings

def parse_to_array(regex_string):
	result={}
	retur=regex_string.split("\r\n")
	for element in retur:
		element2=element.split("=")
		if len(element2)>1:
			result[element2[0].replace("'","")]=element2[1].replace("'","")
	return result
