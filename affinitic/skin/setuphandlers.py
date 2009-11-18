from Products.CMFCore.utils import getToolByName
from Products.Five.component import enableSite
from zope.app.component.interfaces import ISite

LANGUAGES = ['en', 'fr']


def setupVarious(context):
    if context.readDataFile('affinitic.skin_various.txt') is None:
        return

    portal = context.getSite()
    if not ISite.providedBy(portal):
        enableSite(portal)
    setupLanguages(portal)


def setupLanguages(portal):
    lang = getToolByName(portal, 'portal_languages')
    lang.supported_langs = LANGUAGES
    lang.setDefaultLanguage('fr')
    lang.display_flags = 0
