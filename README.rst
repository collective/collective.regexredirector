Introduction
============

SugarCRM_ is an open-source software-solution vendor which produces the Sugar
Customer Relationship Management (CRM) system.

This add-on provide components to use SugarCRM in Plone.

Status
======

Useable in production
Tests in developpement

Components
==========

Regex registry
--------------

A registry is used in order to save regex redirections.
One redirection by line.

'old_url'='new_url'
'old_url2'='new_url2'


Control panel
---------------

To use the registry, you can use the registry configuration or you can use the 
control panel "RegexRedirector".


The redirector
--------------

The utility overiddes plone.app.redirector utility in 404 case.
So first we check by the original utility in RedirectionStorage then we check the 
regex redirector pattern.


INSTALL
=======

Simple installation, you need juste plone.app.redirector ( which is already in the core of Plone )

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
