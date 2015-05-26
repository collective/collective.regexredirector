from zope.component import queryUtility
from zope.interface import implements

from plone.app.redirector.browser import FourOhFourView
from Products.MimetypesRegistry.base_zope import getToolByName

from ..interfaces import IRegexFourOhFourView, IRegexRedirectionStorage


class RegexFourOhFourView(FourOhFourView):

    implements(IRegexFourOhFourView)

    def attempt_redirect(self):
        """
            If 404 try to find a redirection :
            [attempt_redirect of the superclass] and[get on regexredirector
            registry to find regex matching]
        """
        result = super(RegexFourOhFourView, self).attempt_redirect()
        if not result:
            query_string = self.request.QUERY_STRING
            url = self._url()

            if not url:
                return False

            try:
                old_path_elements = self.request.physicalPathFromURL(url)
            except ValueError:
                return False

            old_path = '/'.join(old_path_elements)
            site_path = self.getCurrentSitePath()

            new_path = None
            storage = queryUtility(IRegexRedirectionStorage)

            if storage:
                new_path = storage.get(old_path.replace(site_path, "", 1))
                if new_path and '?' in new_path:
                    (new_path, useless, qs) = new_path.partition('?')
                    if query_string:
                        query_string = '%s&%s' % (qs, query_string)
                    else:
                        query_string = qs
                if new_path:
                    new_path = site_path + new_path

            if not new_path:
                return False

            url = self.request.physicalPathToURL(new_path)

            # re-inject query_string
            if query_string:
                url += "?" + query_string

            self.request.response.redirect(url, status=301, lock=1)
        return True

    def getCurrentSitePath(self):
        portalUrl = getToolByName(self.context, 'portal_url')()
        siteUrl = self.request.physicalPathFromURL(portalUrl)
        return '/'.join(siteUrl)
