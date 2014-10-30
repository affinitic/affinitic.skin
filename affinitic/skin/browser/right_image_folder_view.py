from Products.Five import BrowserView
from zope.interface import implements
from zope.security.interfaces import Unauthorized
from interfaces import IRightImageFolderView


class RightImageFolderView(BrowserView):
    """
    Gestion des images de droite des dossiers de contenu
    """
    implements(IRightImageFolderView)

    def safe_getattr(self, obj, attr, default):
        """Attempts to read the attr, returning default if Unauthorized."""
        try:
            return getattr(obj, attr, default)
        except Unauthorized:
            return default

    def getRightImageContent(self):
        """
        return the right-content background image style regarding folder
        """
        rightImage = self.safe_getattr(self.context, 'right_image.png', None)
        if not rightImage:
            return ""
        rightImageUrl = rightImage.absolute_url()
        style = """<style type="text/css">#content-right-image{background-image:url(%s);}</style>""" % rightImageUrl
        return style
