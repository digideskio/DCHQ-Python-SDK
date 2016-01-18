'''
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied. See the License for the
 specific language governing permissions and limitations
 under the License.

	Author: Amal Francis <amalfra@gmail.com>
'''
import unittest
from dchq.dchq_response import DchqResponse

class Response():
	pass

class DchqResponseTest(unittest.TestCase):
	def test_success(self):
		print 'Running DchqResponse returns success'
		robj = Response()
		robj.status_code = 200
		robj.content = ''

		resp = DchqResponse(robj).success();
		self.assertEqual(resp, True)

	def test_not_success(self):
		print 'Running DchqResponse not return success'
		robj = Response()
		robj.status_code = 404
		robj.content = ''

		resp = DchqResponse(robj).success();
		self.assertEqual(resp, False)

	def test_return_clientError(self):
		print 'Running DchqResponse returns clientError'
		robj = Response()
		robj.status_code = 404
		robj.content = ''
		ret = False

		try:
			DchqResponse(robj).clientError()
		except Exception:
			ret = True

		if ret is False:
			self.fail('No client error thrown')

	def test_not_return_clientError(self):
		print 'Running DchqResponse not return clientError'
		robj = Response()
		robj.status_code = 200
		robj.content = ''
		ret = True

		try:
			DchqResponse(robj).clientError()
		except Exception:
			ret = False

		if ret is False:
			self.fail('Client error thrown')

	def test_return_serverError(self):
		print 'Running DchqResponse returns serverError'
		robj = Response()
		robj.status_code = 500
		robj.content = ''
		ret = False

		try:
			DchqResponse(robj).serverError()
		except Exception:
			ret = True

		if ret is False:
			self.fail('No server error thrown')

	def test_not_return_serverError(self):
		print 'Running DchqResponse not return serverError'
		robj = Response()
		robj.status_code = 200
		robj.content = ''
		ret = True

		try:
			DchqResponse(robj).serverError()
		except Exception:
			ret = False

		if ret is False:
			self.fail('Server error thrown')
