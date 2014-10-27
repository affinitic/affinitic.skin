# -*- coding: utf-8 -*-

from Products.Five.component import enableSite
from zope.component.interfaces import ISite
import logging

logger = logging.getLogger('affinitic.skin')
LANGUAGES = ['fr', 'en']


def setupAffinitic(context):
    logger.debug('Setup Affinitic skin')
    portal = context.getSite()
    if not ISite.providedBy(portal):
        enableSite(portal)
