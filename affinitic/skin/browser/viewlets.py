# -*- coding: utf-8 -*-
"""
affinitic.skin

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: viewlets.py 2141 2008-04-26 17:25:10Z laz $
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from zope.component import getMultiAdapter

class ImageRightContentViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/image_right_content.pt')