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

from dchq_response import DchqResponse
import re
import urllib
import requests
import base64
import json

class DchqRequest:
	def __init__(self, config = {}):
		self.endpoint = 'http://104.130.163.208:33901/api/1.0/';
		self.username = config['username'];
		self.password = config['password'];

	def buildData(self, availableOptions, data):
		query = {};
		i = 0;
		alen = len(availableOptions);
  
		while (i < alen):
			option = availableOptions[i]
			if (option in data):
				query[option] = data[option]
			i = i + 1

		return query;

	def injectParams(self, path = '', params = {}):
		path = "/" + path;
		reg = re.compile('\/:[A-z0-9_-]+')
		fragments = reg.findall(path);
		i = 0;
		alen = len(fragments);

		while(i < alen):
			fragment = fragments[i];
			key = fragment.replace("/:", "");
			if (key not in params):
				raise Exception("Method requires '" + key + "' option.");
			
			path = path.replace(fragment, "/" + params[key]);
			i = i + 1

		path = path.replace('/\\', "");
		return path.replace('\\', "");

	def buildUrl(self, path, urlParams = {}):
		path = self.injectParams(path, urlParams);
		url = self.endpoint + path;
		url = re.sub('\/\/+', '/', url);
		url = url.replace(':/', '://');
		url += "?" + urllib.urlencode(urlParams);
		url = url.replace("/?", "?");
		
		return url;

	def buildRequestConfig(self, resource, data, urlParams):
		config = {};
		config['method'] = resource['method'];
		reqData = self.buildData((resource['options'] if ('options' in resource) else []), data or {});
		config['url'] = self.buildUrl(resource['path'], urlParams);
		auth = "Basic " + base64.b64encode(self.username + ":" + self.password);
		config['headers'] = {
    	'Authorization': auth,
    	'content-type' : 'application/json'
  	};
		config['body'] = json.dumps(reqData);
		
		return config;

	def process(self, resource, opts = {}, urlParams = {}):
		config = self.buildRequestConfig(resource, opts, urlParams);

		if config['method'] == 'GET':
			resp = requests.get(config['url'], data=config['body'], headers=config['headers'])
		elif config['method'] == 'POST':
			resp = requests.post(config['url'], data=config['body'], headers=config['headers'])
		elif config['method'] == 'PUT':
			resp = requests.put(config['url'], data=config['body'], headers=config['headers'])
		elif config['method'] == 'DELETE':
			resp = requests.delete(config['url'], data=config['body'], headers=config['headers'])
		else:
			raise Exception('Unknown HTTP method')

		response = DchqResponse(resp)

		if response.success():
			return json.loads(resp.content)
		elif response.clientError():
			response.clientError()
		elif response.serverError():
			response.serverError()
		else:
			raise Exception('Failed to process response')
