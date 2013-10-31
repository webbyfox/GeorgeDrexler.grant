from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class GeorgedrexlergrantLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import georgedrexler.grant
        xmlconfig.file(
            'configure.zcml',
            georgedrexler.grant,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'georgedrexler.grant:default')

GEORGEDREXLER_GRANT_FIXTURE = GeorgedrexlergrantLayer()
GEORGEDREXLER_GRANT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GEORGEDREXLER_GRANT_FIXTURE,),
    name="GeorgedrexlergrantLayer:Integration"
)
GEORGEDREXLER_GRANT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GEORGEDREXLER_GRANT_FIXTURE, z2.ZSERVER_FIXTURE),
    name="GeorgedrexlergrantLayer:Functional"
)
