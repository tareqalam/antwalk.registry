# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import antwalk.registry


class AntwalkRegistryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=antwalk.registry)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "antwalk.registry:default")


ANTWALK_REGISTRY_FIXTURE = AntwalkRegistryLayer()


ANTWALK_REGISTRY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ANTWALK_REGISTRY_FIXTURE,),
    name="AntwalkRegistryLayer:IntegrationTesting",
)


ANTWALK_REGISTRY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ANTWALK_REGISTRY_FIXTURE,),
    name="AntwalkRegistryLayer:FunctionalTesting",
)


ANTWALK_REGISTRY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ANTWALK_REGISTRY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="AntwalkRegistryLayer:AcceptanceTesting",
)
