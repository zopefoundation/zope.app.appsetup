##############################################################################
#
# Copyright (c) 2002, 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Bootstrap code.

This module contains code to bootstrap a Zope3 instance.  For example
it makes sure a root folder exists and creates one if necessary.
"""
import logging
import warnings

import transaction
import zope.component.interfaces
import zope.event
import zope.lifecycleevent
import zope.processlifetime
from zope.app.publication.zopepublication import ZopePublication
from zope.container.interfaces import INameChooser
from zope.security.management import getSecurityPolicy
from zope.security.simplepolicies import ParanoidSecurityPolicy
from zope.site import site
from zope.site.folder import rootFolder
from zope.traversing.api import traverse


_marker = object()


def ensureObject(root_folder, object_name, object_type, object_factory,
                 asObject=_marker):
    """Check that there's a basic object in the site manager. If not, add one.

    Return the name abdded, if we added an object, otherwise None.
    """
    if asObject is not _marker:
        warnings.warn("asObject argument is deprecated and will be "
                      "removed in Zope 3.6", DeprecationWarning, 2)

    package = getSiteManagerDefault(root_folder)
    valid_objects = [name
                     for name in package
                     if object_type.providedBy(package[name])]
    if valid_objects:
        return None
    name = object_name
    obj = object_factory()
    package[name] = obj
    return obj


def ensureUtility(root_folder, interface, utility_type,
                  utility_factory, name='', asObject=_marker, **kw):
    """Add a utility to the top site manager

    Returns the name added or ``None`` if nothing was added.
    """
    if asObject is not _marker:
        warnings.warn("asObject argument is deprecated and will be "
                      "removed in Zope 3.6", DeprecationWarning, 2)

    sm = root_folder.getSiteManager()
    utils = [reg for reg in sm.registeredUtilities()
             if (reg.provided.isOrExtends(interface) and reg.name == name)]
    if len(utils) == 0:
        return addConfigureUtility(
            root_folder, interface, utility_type, utility_factory,
            name, asObject, **kw)
    else:
        return None


def addConfigureUtility(
        root_folder, interface, utility_type, utility_factory, name='',
        asObject=_marker, **kw):
    """Add and configure a utility to the root folder."""
    if asObject is not _marker:
        warnings.warn("asObject argument is deprecated and will be "
                      "removed in Zope 3.6", DeprecationWarning, 2)

    utility = addUtility(root_folder, utility_type, utility_factory, **kw)
    root_folder.getSiteManager().registerUtility(utility, interface, name)
    return utility


def addUtility(root_folder, utility_type, utility_factory,
               asObject=_marker, **kw):
    """Add a Utility to the root folder's site manager.

    The utility is added to the default package and activated.
    """
    if asObject is not _marker:
        warnings.warn("asObject argument is deprecated and will be "
                      "removed in Zope 3.6", DeprecationWarning, 2)

    package = getSiteManagerDefault(root_folder)
    chooser = INameChooser(package)
    utility = utility_factory()
    name = chooser.chooseName(utility_type, utility)
    package[name] = utility

    # the utility might have been location-proxied; we need the name
    # information (__name__) so let's get it back again from the
    # container
    utility = package[name]

    # Set additional attributes on the utility
    for k, v in kw.items():
        setattr(utility, k, v)
    return utility


def getSiteManagerDefault(root_folder):
    package = traverse(root_folder.getSiteManager(), 'default')
    return package


def getInformationFromEvent(event):
    """Extract information from the event

    Return a tuple containing

      - db
      - connection open from the db
      - root connection object
      - the root_folder object
    """
    db = event.database
    connection = db.open()
    root = connection.root()
    root_folder = root.get(ZopePublication.root_name, None)
    return db, connection, root, root_folder


######################################################################
######################################################################

def bootStrapSubscriber(event):
    """The actual subscriber to the bootstrap IDataBaseOpenedEvent

    Boostrap a Zope3 instance given a database object This first checks if the
    root folder exists and has a site manager.  If it exists, nothing else
    is changed.  If no root folder exists, one is added.
    """
    db, connection, root, root_folder = getInformationFromEvent(event)

    if root_folder is None:
        # ugh... we depend on the root folder implementation
        root_folder = rootFolder()
        zope.event.notify(zope.lifecycleevent.ObjectCreatedEvent(root_folder))
        root[ZopePublication.root_name] = root_folder
        if not zope.component.interfaces.ISite.providedBy(root_folder):
            site_manager = site.LocalSiteManager(root_folder)
            root_folder.setSiteManager(site_manager)

        transaction.commit()

    connection.close()

    zope.event.notify(zope.processlifetime.DatabaseOpenedWithRoot(db))


########################################################################
########################################################################

def checkSecurityPolicy(event):
    """Warn if the configured security policy is ParanoidSecurityPolicy

    Between Zope X3 3.0 and Zope 3.1, the security policy configuration
    was refactored and now it needs to be included from site.zcml.
    """
    if getSecurityPolicy() is ParanoidSecurityPolicy:
        logging.getLogger('zope.app.appsetup').warning(
            'Security policy is not configured.\n'
            'Please make sure that securitypolicy.zcml is included'
            ' in site.zcml immediately\n'
            'before principals.zcml')
