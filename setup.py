# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='affinitic.skin',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
      ],
      keywords='',
      author='Affinitic',
      author_email='support@lists.affinitic.be',
      url='https://github.com/affinitic/affinitic.core',
      license='gpl',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
