##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
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
"""Setup for zope.app.appsetup package

$Id$
"""

import os

from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='zope.app.appsetup',
    version = '3.4.0',
    author='Zope Corporation and Contributors',
    author_email='zope3-dev@zope.org',
    description = "Zope app setup helper",
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    license='ZPL 2.1',
    keywords = "zope3 app setup",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    url='http://cheeseshop.python.org/pypi/zope.app.appsetup',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    extras_require=dict(test=['zope.app.testing']),
    namespace_packages=['zope', 'zope.app'],
    install_requires=['setuptools',
                      'zope.interface',
                      'zope.security',
                      'zope.component',
                      'zope.app.component',
                      'zope.app.folder',
                      'zope.configuration',
                      'zope.event',
                      'zope.traversing',
                      'zope.app.container',
                      'zope.app.publication',
                      'ZODB3',
                      ],
    include_package_data = True,
    zip_safe = False,
    )
