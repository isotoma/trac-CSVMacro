#!/usr/bin/env python
# $Id$
#
# Copyright 2010 Isotoma
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" 
Trac CSV Macro set up config
"""

__author__ = 'Ben Miller <ben.miller@isotoma.com>'
__docformat__ = 'restructuredtext en'
__version__ = '$Revision$'[11:-2]

from setuptools import setup

setup(
    name = 'CSVMacro',
    version = __version__,
    packages = ['csvmacro'],
    package_data = { 'csvmacro': [] },
    author = __author__.split(' <')[:1],
    author_email = __author__.split(' <')[1:][0].rstrip('>'),
    description = 'Macro for reading CSV files and displaying the results as a table on the wiki page',
    url = 'http://github.com/isotoma/trac-CSVMacro',
    license = 'Apache2',
    classifiers = ['Framework :: Trac'],
    entry_points = {
        'trac.plugins': 
            ['csvmacro = csvmacro'
        ]
    }
)
