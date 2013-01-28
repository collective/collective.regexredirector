from plone.testing import z2

from plone.app.testing import *
import collective.regexredirector

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=collective.regexredirector,
                                additional_z2_products=[],
                                gs_profile_id='collective.regexredirector:default',
                                name="collective.regexredirector:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.regexredirector:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.regexredirector:Functional")

