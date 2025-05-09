Changelog
=========

5.1 (unreleased)
----------------

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-02-09)
----------------

- Add support for Python 3.9, 3.10, 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


4.2.0 (2020-05-20)
------------------

- Drop support for ``python setup.py test``.

- Add support for Python 3.8.

- Drop support for Python 3.4.


4.1.0 (2018-12-15)
------------------

- Add support for Python 3.6, 3.7 and PyPy3.

- Drop support for Python 3.3.


4.0.0 (2016-08-08)
------------------

- Add dependency on ``zdaemon`` (split off from ``ZODB``).

- Claim support for Python 3.4, 3.5 and PyPy which requires
  ``zope.app.publication`` >= 4.0.

- Drop Python 2.6 support.

4.0.0a1 (2013-03-03)
--------------------

- Added support for Python 3.3.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


3.16.0 (2011-01-27)
-------------------

- Added stacking of storages for layer/test level setup separation in derived
  ZODBLayers.


3.15.0 (2010-09-25)
-------------------

- Updated tests to run with `zope.testing >= 3.10`, requiring at least this
  version and `zope.testrunner`.

- Switch ``IErrorReportingUtility copy_to_zlog`` field to ``True``.

- Using Python's `doctest` module instead of depreacted
  `zope.testing.doctest`.


3.14.0 (2010-04-13)
-------------------

- Made `zope.testing` an optional (test) dependency.

- Removed test dependency on `zope.app.testing`.


3.13.0 (2009-12-24)
-------------------

- Import hooks functionality from zope.component after it was moved there from
  zope.site.

- Import ISite from zope.component after it was moved there from
  zope.location. This lifts the dependency on zope.location.

- Added missing install dependency on `zope.testing`.


3.12.0 (2009-06-20)
-------------------

- Using ``zope.processlifetime`` interfaces and implementations
  directly instead of BBB imports from ``zope.app.appsetup``.

- Got rid of depencency on ``zope.app.component``.

- Got rid of test dependency on ``zope.app.security``.


3.11 (2009-05-13)
-----------------

- Event interfaces / implementations moved to ``zope.processlifetime``,
  version 1.0.  Depend on this package, and add BBB imports.


3.10.1 (2009-03-31)
-------------------

- Fixed a ``DeprecationWarning`` introduced in 3.10.0.

- Added doctests to long description to show up at pypi.


3.10.0 (2009-03-19)
-------------------

- Finally deprecate the "asObject" argument of helper functions in the
  ``zope.app.appsetup.bootstrap`` module. If your code uses any of these
  functions, please remove the "asObject=True" argument passing anywhere,
  because the support for that argument will be dropped soon.

- Move session utility bootstrapping logic from ``zope.session`` into this
  package. This removes a dependency from zope.session to this package.

- Remove one more deprecated function.


3.9.0 (2009-01-31)
------------------

- Use ``zope.site`` instead of ``zope.app.folder`` and
  ``zope.app.component``.

- Use ``zope.container`` instead of ``zope.app.container``.

- Move error log bootstrapping logic from ``zope.error`` into this
  package.  This removes a dependency from zope.error to this
  package. Also added a test for bootstrapping the error log here,
  which was missing in ``zope.error``.


3.8.0 (2008-08-25)
------------------

- Feature: Developed an entry point that allows you to quickly bring up an
  application instance for debugging purposes. (Implemented by Marius Gedminas
  and Stephan Richter.)


3.7.0 (2008-08-19)
------------------

- Added ``.product.loadConfiguration`` test-support function; loads product
  configuration (only) from a file object, allowing test code (including
  setup) to make use of the same configuration schema support used by normal
  startup.


3.6.0 (2008-07-23)
------------------

- Added additional test support functions to set the configuration for a
  single section, and save/restore the entire configuration.


3.5.0 (2008-06-17)
------------------

- Added helper class for supporting product configuration tests.

- Added documentation for the product configuration API, with tests.


3.4.1 (2007-09-27)
------------------

- Egg was faulty, re-released.


3.4.0 (2007-09-25)
------------------

- Initial documented release.

- Reflect changes form zope.app.error refactoring.
