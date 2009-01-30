# -*- coding: utf-8 -*-
"""
Affinitic.skin

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: viewlets.py 4075 2009-01-19 14:53:19Z schminitz $
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping


class AffiniticHeaderViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/headerAffinitic.pt')


class AffiniticContentViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/contentAffinitic.pt')

    def bouge(self):
        context = self.context
        site = context.getSite()
        column = getUtility(IPortletManager, name=u'plone.leftcolumn', context=site)
        manager = getMultiAdapter((site, column, ), IPortletAssignmentMapping)
        for portlet in manager:
            del manager[portlet]

class AffiniticFooterViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/footerAffinitic.pt')
