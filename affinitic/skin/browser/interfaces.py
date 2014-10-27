# -*- coding: utf-8 -*-

from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IAffiniticTheme(IDefaultPloneLayer):
    """
    Theme for Affinitic
    """


class IRightImageFolderView(Interface):
    """
    Gestion des images à droite des folder contenu infos
    """

    def getRightImageContent():
        """
        return the right image for a folder
        """
