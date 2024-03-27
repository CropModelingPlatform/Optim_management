#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from os import walk
from os.path import abspath, normpath, splitext
from os.path import join as pj

from setuptools import setup, find_packages



short_descr = "gridded crop models inputs extracting and processing library"
readme = open('README.md').read()
history = open('HISTORY.rst').read()
url = "https://gitlab.cirad.fr/modelingplatform/spatialweatherapi"

description = ''
long_description = '''
gridded crop models inputs extracting and processing library.
'''



_version = {}
with open("src/spatialweatherapi/version.py") as fp:
    exec(fp.read(), _version)
    version = _version["__version__"]

# find packages
pkgs = find_packages('src')

pkg_data = {}

nb = len(normpath(abspath("src/spatialweatherapi"))) + 1
data_rel_pth = lambda pth: normpath(abspath(pth))[nb:]

data_files = []
for root, dnames, fnames in walk("src/spatialweatherapi"):
    for name in fnames:
        if splitext(name)[-1] in [u'.json', u'.xml', u'.ini', u".sh", u".shp"]:
            data_files.append(data_rel_pth(pj(root, name)))


pkg_data['spatialweatherapi'] = data_files

setup_kwds = dict(
    name='spatialweatherapi',
    version=version,
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="Cyrille Ahmed Midingoyi",
    author_email="cyrille_ahmed.midingoyi@cirad.fr",
    url=url,
    license='MIT',
    zip_safe=False,
    packages=pkgs,
    package_dir={'': 'src'},
    
    
    package_data=pkg_data,
    setup_requires=[
        ],
    install_requires=[
        ],
    tests_require=[
        "pytest",
        ],
    entry_points={},
    keywords='',
    )
# #}
# change setup_kwds below before the next pkglts tag

setup_kwds["entry_points"] = {"console_scripts": ["clim = spatialweatherapi.main:main"]}

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
