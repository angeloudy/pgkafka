#!/usr/bin/env python

from setuptools import setup

setup(name='pgkafka',
      version='0.1',
      description='Stream os metrics through kafka to psql',
      author='laocius',
      author_email='zhoutao@laocius.org',
      url='http://github.com/angeloudy/',
      license='GPL-3',
      packages=['pgkafka'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Operating System :: POSIX',
          'Programming Language :: Python3.7'],
      test_suite="tests",
      install_requires=[
          "kafka-python",
          "psycopg2"]
      )
