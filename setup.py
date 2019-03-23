#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name = 'addsshkeys',
    version = '0.0.2',
    author = 'Ken Kundert',
    author_email = 'addsshkeys@nurdletech.com',
    description = 'Add keys to SSH Agent',
    long_description = readme,
    url = 'https://github.com/kenkundert/addsshkeys',
    download_url = 'https://github.com/kenkundert/addsshkeys/tarball/master',
    license = 'GPLv3+',
    scripts = 'addsshkeys'.split(),
    install_requires = [
        'appdirs',
        'avendesora>=1.12',
        'docopt',
        'inform>=1.14',
    ],
    python_requires='>=3.6',
    keywords = 'avendesora ssh'.split(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
