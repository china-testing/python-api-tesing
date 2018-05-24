#!/usr/bin/python
# (c) 2005-2009 Divmod, Inc.  See LICENSE file for details

from distutils.core import setup

setup(
    name="hello_world",
    license="MIT",
    version="1.0.0",
    description="Sample program to test CI engines",
    packages=["hello"],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
        ])
