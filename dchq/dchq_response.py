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

class DchqResponse:
	def __init__(self, res):
		self.body = res.content
		self.statusCode = res.status_code

	def success(self):
		return self.statusCode >= 200 and self.statusCode <= 299

	def clientError(self):
		if (self.statusCode >= 400 and self.statusCode <= 499):
			raise Exception("HTTP client error " + str(self.statusCode))

	def serverError(self):
		if (self.statusCode >= 500 and self.statusCode <= 599):
			raise Exception("HTTP server error " + str(self.statusCode));
