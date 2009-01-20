from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IAffiniticTheme(IDefaultPloneLayer):
    """
    Theme for Affinitic
    """


class IHomePageNews(Interface):
    """
    Gestion des viewlets sur la homepage
    """
