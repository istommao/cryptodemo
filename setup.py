# -*- coding: utf-8 -*-
"""setup.py."""

from setuptools import setup, find_packages

VERSION = '0.0.1'

LONG_DESCRIPTION = 'cryptography practice demo.'

setup(
    name='cryptodemo',
    version=VERSION,
    description='cryptography practice demo.',
    long_description=LONG_DESCRIPTION,
    author='silence',
    author_email='istommao@gmail.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/istommao/cryptodemo',
    keywords='cryptography practice demo!'
)
