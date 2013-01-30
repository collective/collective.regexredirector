Introduction
============

collective.regexredirector extends the plone.app.redirector behavior to allow to define redirections
using regular expressions.

It might be particulary useful if you migrate an old website and you want to map old urls to the new
site structure.


Note: when a 404 occurs, collective.regexredirector first calls plone.app.redirector, and if it does not
redirect, then collective.regexredirector tries to match one of its registered regular expressions.

Usage
=====

In the Plone control panel, go to the "RegexRedirector" control panel and enter your redirection rules.

One redirection by line using the following format ::

    'old_url'='new_url'
    'old_url2'='new_url2'


Examples
--------

Redirecting all urls like /news/something to /archives/index ::

    '/news/.*'='/archives/index'

Redirecting all urls like /tags/something to /category/something ::

    '/tags/(?P<category_name>.+)'='/category/\g<category_name>/view'


INSTALL
=======

Add collective.regexredirector to your buildout eggs.

Credits
=======

Companies
---------

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_


Authors
-------

- Julien Marinescu davisp1 <davisp@xenbox.fr>

.. Contributors

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
