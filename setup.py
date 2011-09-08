#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='presence',
      version='0.1',
      packages=find_packages(),
      package_data={'presence': ['bin/*.*',]},
      exclude_package_data={'presence': ['bin/*.pyc']},
      scripts=['presence/bin/manage.py'])
