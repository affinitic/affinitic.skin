from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping


def setupAffinitic(context):
    site = context.getSite()
    left = getUtility(IPortletManager, name=u'plone.leftcolumn', context=site)
    leftColumn = getMultiAdapter((site, left, ), IPortletAssignmentMapping, context=context)
    right = getUtility(IPortletManager, name=u'plone.rightcolumn', context=site)
    rightColumn = getMultiAdapter((site, right, ), IPortletAssignmentMapping, context=context)
    for portlet in leftColumn:
        del leftColumn[portlet]
    for portlet in rightColumn:
        del rightColumn[portlet]


#def setupAffinitic_back(context):
#    portal = context.getSite()
#    affinitic = createAffiniticFolder(portal)
#    clearPortlets(affinitic)
#
#
#def createAffiniticFolder(portal):
#    if not portal.hasObject('affinitic'):
#        portal.invokeFactory('Folder', 'affinitic')
#    return getattr(portal, 'affinitic')
#
#
#def getManager(folder, column):
#    if column == 'left':
#        manager = getUtility(IPortletManager, name=u'plone.leftcolumn', context=folder)
#    else:
#        manager = getUtility(IPortletManager, name=u'plone.rightcolumn', context=folder)
#    return manager
#
#
#def clearColumnPortlets(folder, column):
#    manager = getManager(folder, column)
#    assignments = getMultiAdapter((folder, manager, ), IPortletAssignmentMapping)
#    for portlet in assignments:
#        del assignments[portlet]
#
#
#def clearPortlets(folder):
#    clearColumnPortlets(folder, 'left')
#    clearColumnPortlets(folder, 'right')
#
#
#def clearPortlets_back(folder):
#    if not folder.hasProperty('left_slots'):
#        folder.manage_addProperty('left_slots', [], 'lines')
#    if not folder.hasProperty('right_slots'):
#        folder.manage_addProperty('right_slots', [], 'lines')
#    folder.manage_changeProperties(left_slots=[],
#                                   right_slots=[])
