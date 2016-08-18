#!/usr/bin/env python

import sys
from setuptools import setup

additional_reqs = []
if sys.platform == "darwin":
    additional_reqs.append("pyobjc-framework-Quartz")


setup(name='aw-watcher-afk',
      version='0.1',
      description='AFK watcher for ActivityWatch',
      author='Erik Bjäreholt',
      author_email='erik@bjareho.lt',
      url='https://github.com/ActivityWatch/aw-watcher-afk',
      packages=['aw_watcher_afk'],
      install_requires=[
          'aw-client',
          'pyuserinput',
          'pytz',
          'python-xlib',
      ] + additional_reqs,
      dependency_links=[
          'https://github.com/python-xlib/python-xlib/tarball/master#egg=python-xlib',
          'https://github.com/ActivityWatch/aw-client/tarball/master#egg=aw-client'
      ],
      entry_points={
          'console_scripts': ['aw-watcher-afk = aw_watcher_afk:main']
      })
