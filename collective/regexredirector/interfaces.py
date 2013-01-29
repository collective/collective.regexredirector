from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory
from plone.app.redirector.interfaces import IRedirectionStorage, IFourOhFourView

_ = MessageFactory('collective.regexredirector')


class IRegexSettings(Interface):
    """Global regexredirector settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
	
	In order to use it, the pattern is 'url_old_with_regex'='new_url'"+

    example1 :
    '/tags/(?P<category_name>.+)'='/category/\g<category_name>/view' 
    >>s='/tags/plone' 
    >>re.sub('/tags/(?P<category_name>.+)', '/category/\g<category_name>/view', s)
      =>    '/category/plone/view' 

    example2 :
    '/tags/.*'='/archives/index' : 
    >>re.sub('/tags/.*', '/archives/index', s) 
      =>    '/archives/index'
    """

    regex_values = schema.Text(title=_(u"Redirection using regex"),
                               description=_(u"In order to use it, the pattern is 'url_old_with_regex'='new_url' \n "+
                               " ( example1 : s='/tags/plone' >>re.sub('/tags/(?P<category_name>.+)', '/category/\g<category_name>/view', s) "+
                               " => '/category/plone/view' )    \n"+
                               " ( example2 : >>re.sub('/tags/.*', '/archives/index', s) =>'/archives/index' )"),
                               required=False,
                               default=u'',)

class IRegexRedirectionStorage(IRedirectionStorage):
    """
    """
    
class IRegexFourOhFourView(IFourOhFourView):
    """
    """