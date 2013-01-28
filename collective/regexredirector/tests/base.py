import transaction
import unittest2 as unittest
from zope import interface
from plone.app import testing
from collective.regexredirector import testing
from Products.PloneTestCase import PloneTestCase

class UnitTestCase(unittest.TestCase):

    def setUp(self):
        pass

class RedirectorTestCase(PloneTestCase.PloneTestCase):
    pass

