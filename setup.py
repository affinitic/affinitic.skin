from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='affinitic.skin',
      version=version,
      description="Skin for Affinitic public website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme skin affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='http://svn.affinitic.be/plone/affinitic/affinitic.skin/trunk/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['affinitic'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'plone.app.themingplugins',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
