#!/usr/bin/env python

from codecs import open

from setuptools import setup

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="addsshkeys",
    version="0.4.0",
    author="Ken Kundert",
    author_email="addsshkeys@nurdletech.com",
    description="Add keys to SSH Agent",
    long_description=readme,
    long_description_content_type = 'text/x-rst',
    url="https://github.com/kenkundert/addsshkeys",
    download_url="https://github.com/kenkundert/addsshkeys/tarball/master",
    license="GPLv3+",
    scripts="addsshkeys".split(),
    install_requires=[
        "appdirs",
        "avendesora>=1.12",
        "docopt",
        "inform>=1.14",
        "nestedtext>=1.1",
        "pexpect",
    ],
    python_requires=">=3.6",
    keywords="avendesora ssh".split(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
