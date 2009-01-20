# -*- coding: utf-8 -*-
"""
Affinitic.skin

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: viewlets.py 4075 2009-01-19 14:53:19Z schminitz $
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet


class AffiniticHeaderViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/headerAffinitic.pt')


class AffiniticContentViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/contentAffinitic.pt')


class AffiniticFooterViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/footerAffinitic.pt')
