#!/usr/bin/env python

from setuptools import setup

setup(name='matheval',
      version='0.1',
      description='Evaluation of expression trees',
      author='Moritz Lenz',
      author_email='moritz.lenz@gmail.com',
      url='https://deploybook.com/',
      requires=['flask', 'pytest', 'gunicorn'],
      setup_requires=['pytest-runner'],
      packages=['matheval']
     )
