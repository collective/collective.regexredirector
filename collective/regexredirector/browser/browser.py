from zope.component import queryUtility
from zope.interface import implements

from plone.app.redirector.browser import FourOhFourView
from Products.MimetypesRegistry.base_zope import getToolByName

from collective.regexredirector.interfaces import IRegexFourOhFourView,IRegexRedirectionStorage

class RegexFourOhFourView(FourOhFourView):

    implements(IRegexFourOhFourView)
    
    def attempt_redirect(self):
        """
            If 404 try to find a redirection : 
            [attempt_redirect of the superclass] and [get on regexredirector registry to find regex matching]
        """
        result=super(RegexFourOhFourView, self).attempt_redirect()
        if result==False:
            query_string = self.request.QUERY_STRING
            url = self._url()

            if not url:
                return False

            try:
                old_path_elements = self.request.physicalPathFromURL(url)
            except ValueError:
                return False

            old_path = '/'.join(old_path_elements)
            site_path=self.getCurrentSitePath()

            new_path = None
            storage=queryUtility(IRegexRedirectionStorage)
            
            if storage is not None:
                new_path=storage.get(old_path.replace(site_path,"",1))
                if new_path:
                    new_path=site_path+new_path

            if not new_path:
                return False

            url = self.request.physicalPathToURL(new_path)

            # some analytics programs might use this info to track
            if query_string:
                url += "?"+query_string

            self.request.response.redirect(url, status=301, lock=1)
        return True
    
    def getCurrentSitePath(self):
        portalUrl = getToolByName(self.context, 'portal_url')()
        siteUrl=self.request.physicalPathFromURL(portalUrl)
        return '/'.join(siteUrl)