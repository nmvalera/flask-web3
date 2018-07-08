"""
    Flask-Web3
    ~~~~~~~~~~

    Flask extension allowing to smoothly integrate with web3.py

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see LICENSE for more details.
"""

import os

from setuptools import setup, find_packages


def read(file_name):
    try:
        return open(os.path.join(os.path.dirname(__file__), file_name)).read()
    except FileNotFoundError:
        return ''


setup(
    name='Flask-Web3',
    version='0.1.1',
    license=read('LICENSE'),
    url='https://github.com/nmvalera/flask-web3',
    author='Nicolas Maurice',
    author_email='nicolas.maurice.valera@gmail.com',
    maintainer='ConsenSys France',
    description='Flask extension allowing to smoothly integrate with web3.py.',
    long_description=read('README.rst'),
    packages=find_packages(),
    install_requires=[
        'web3>=4.4.0',
        'flask>=1.0.0',
    ],
    extras_require={
        'dev': [
            'flake8',
            'autoflake',
            'autopep8',
            'coverage',
            "eth-tester[py-evm]==0.1.0-beta.26",
            'pytest>=3',
            'tox',
            'sphinx',
            'sphinx_rtd_theme',
        ],
        'doc': [
            'sphinx',
            'sphinx_rtd_theme',
        ],
    },
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests'
)
