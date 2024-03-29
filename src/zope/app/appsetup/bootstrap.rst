Bootstrap helpers
=================

The bootstrap helpers provide a number of functions that help with
bootstrapping.

The bootStrapSubscriber function makes sure that there is a root
object.  It subscribes to DatabaseOpened events:

    >>> from zope.app.appsetup import bootstrap
    >>> import zope.processlifetime

    >>> from ZODB.MappingStorage import DB
    >>> db = DB()
    >>> bootstrap.bootStrapSubscriber(zope.processlifetime.DatabaseOpened(db))

The subscriber makes sure that there is a root folder:

    >>> from zope.app.publication.zopepublication import ZopePublication
    >>> conn = db.open()
    >>> root = conn.root()[ZopePublication.root_name]
    >>> sm = root.getSiteManager()
    >>> conn.close()

A DatabaseOpenedWithRoot is generated with the database.

    >>> from zope.component.eventtesting import getEvents
    >>> [event] = getEvents(zope.processlifetime.IDatabaseOpenedWithRoot)
    >>> event.database is db
    True

Generally, startup code that expects the root object and site to have
been created will want to subscribe to this event, not
IDataBaseOpenedEvent.

The subscriber generates the event whether or not the root had to be
set up:

    >>> bootstrap.bootStrapSubscriber(zope.processlifetime.DatabaseOpened(db))
    >>> [e, event] = getEvents(zope.processlifetime.IDatabaseOpenedWithRoot)
    >>> event.database is db
    True


Check the Security Policy
-------------------------

When the security policy got refactored to be really pluggable, the
inclusion of the security policy configuration was moved to the very
top level, to site.zcml.  This happened in r24770, after ZopeX3 3.0
was released, but before 3.1.

Now the maintainers of existing 3.0 sites need to manually update
their site.zcml to include securitypolicy.zcml while upgrading to 3.1.
See also http://www.zope.org/Collectors/Zope3-dev/381 .

    >>> from zope.testing.loggingsupport import InstalledHandler
    >>> handler = InstalledHandler('zope.app.appsetup')

If the security policy is unset from the default
ParanoidSecurityPolicy, we get a warning:

    >>> from zope.app.appsetup.bootstrap import checkSecurityPolicy
    >>> event = object()
    >>> checkSecurityPolicy(event)
    >>> print(handler)
    zope.app.appsetup WARNING
      Security policy is not configured.
    Please make sure that securitypolicy.zcml is included in site.zcml immediately
    before principals.zcml

However, if any non-default security policy is installed, no warning
is emitted:

    >>> from zope.security.management import setSecurityPolicy
    >>> defaultPolicy = setSecurityPolicy(object())
    >>> handler.clear()
    >>> checkSecurityPolicy(event)
    >>> print(handler)
    <BLANKLINE>

Clean up:

    >>> handler.uninstall()
