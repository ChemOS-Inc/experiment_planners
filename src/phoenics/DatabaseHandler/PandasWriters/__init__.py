#!/usr/bin/env python

'''
Licensed to the Apache Software Foundation (ASF) under one or more 
contributor license agreements. See the NOTICE file distributed with this 
work for additional information regarding copyright ownership. The ASF 
licenses this file to you under the Apache License, Version 2.0 (the 
"License"); you may not use this file except in compliance with the 
License. You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
License for the specific language governing permissions and limitations 
under the License.

The code in this file was developed at ChemOS Inc. (2019).
'''

__author__  = 'Florian Hase'

#=========================================================================

import sys

from utilities import PhoenicsModuleError

#=======================================================================

try:
	import pandas
except ModuleNotFoundError:
	_, error_message, _ = sys.exc_info()
	extension = '\n\tTry installing the pandas package of use a different database output format (e.g. pickle).'
	PhoenicsModuleError(str(error_message) + extension)

try:
	import openpyxl
except ModuleNotFoundError:
	_, error_message, _ = sys.exc_info()
	extension = '\n\tWriting to xlsx requires the openpyxl package. Please install the package or choose a different output format (e.g. csv or pickle)'
	PhoenicsModuleError(str(error_message) + extension)

#=======================================================================

from DatabaseHandler.PandasWriters.db_writer import DB_Writer

