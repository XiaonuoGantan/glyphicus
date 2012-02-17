#!/usr/bin/env python
import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'SQLAlchemy',
    'flask',
    'zope.sqlalchemy',
    'webtest',
    'redis',
    'nose',
    'psycopg2',
]


setup(name='glyphicus',
      version='0.0',
      description='glyphicus',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Xiaonuo Gantan',
      author_email='xiaonuo.gantan@gmail.com',
      url='www.github.com/XiaonuoGantan/glyphicus',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages('.'),
      include_package_data=True,
      zip_safe=False,
      test_suite='browzoo_app',
      install_requires = requires,
)
