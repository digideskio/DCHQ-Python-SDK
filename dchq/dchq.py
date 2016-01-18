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

from dchq_request import DchqRequest
import json
import os

class Dchq:
	def __init__(self, config={}):
		if 'username' not in config:
			raise Exception("Username must be provided");

		if 'password' not in config:
			raise Exception("Password must be provided");

		self.request = DchqRequest(config);
		self.routes_cats = ['blueprints', 'datacenters', 'builds', 'dockerservers', 'apps', 'usergroups', 'profiles', 			'messages', 'users', 'plugins', 'cloudproviders', 'registryaccounts', 'settings'];
		self.routes = {};
		
		__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		for it in self.routes_cats:
			with open(os.path.join(__location__, './routes/' + it + '.json')) as data_file:    
				self.routes[it] = json.load(data_file);	

	# Blueprints
	def getBlueprints(self):
		return self.request.process(self.routes['blueprints']['getBlueprints']);

	def createBlueprint(self, data):
		return self.request.process(self.routes['blueprints']['createBlueprint'], data);

	def getBlueprintsManage(self, data = {}):
		return self.request.process(self.routes['blueprints']['getBlueprintsManage'], data);

	def getBlueprintsManageById(self, id):
		return self.request.process(self.routes['blueprints']['getBlueprintsManageById'], {}, {'id': id});

	def searchBlueprintsLibraryPage(self, data = {}):
		return self.request.process(self.routes['blueprints']['searchBlueprintsLibraryPage'], data, {'q': data['q']});

	def getBlueprintById(self, id):
		return self.request.process(self.routes['blueprints']['getBlueprintById'], {}, {'id': id});

	def updateBlueprintById(self, id, data = {}):
		return self.request.process(self.routes['blueprints']['updateBlueprintById'], data, {'id': id});

	def deleteBlueprintById(self, id):
		return self.request.process(self.routes['blueprints']['deleteBlueprintById'], {}, {'id': id});

	def starBlueprintById(self, id):
		return self.request.process(self.routes['blueprints']['starBlueprintById'], {}, {'id': id});

	def unstarBlueprintById(self, id):
		return self.request.process(self.routes['blueprints']['unstarBlueprintById'], {}, {'id': id});

	def getStarredBlueprints(self):
		return self.request.process(self.routes['blueprints']['getStarredBlueprints']);

	def getBlueprintYamlById(self, id):
		return self.request.process(self.routes['blueprints']['getBlueprintYamlById'], {}, {'id': id});

	# Datacenters
	def getDatacenters(self):
		return self.request.process(self.routes['datacenters']['getDatacenters']);

	def getDatacenterById(self, id):
		return self.request.process(self.routes['datacenters']['getDatacenterById'], {}, {'id': id});

	def createDatacenter(self, data = {}):
		return self.request.process(self.routes['datacenters']['createDatacenter'], data);

	def updateDatacenterById(self, id, data = {}):
		return self.request.process(self.routes['datacenters']['updateDatacenterById'], data, {'id': id});

	def deleteDatacenterById(self, id):
		return self.request.process(self.routes['datacenters']['deleteDatacenterById'], {}, {'id': id});

	def getDatacentersManage(self):
		return self.request.process(self.routes['datacenters']['getDatacentersManage']);

	def searchDatacenters(self, data = {}):
		return self.request.process(self.routes['datacenters']['searchDatacenters'], data, {'q': data['q']});

	# Builds
	def getBuilds(self):
		return self.request.process(self.routes['builds']['getBuilds']);

	def getBuildsManage(self, data = {}):
		return self.request.process(self.routes['builds']['getBuildsManage'], data);

	def getBuildsManageById(self, id):
		return self.request.process(self.routes['builds']['getBuildsManageById'], {}, {'id': id});

	def searchBuilds(self, data = {}):
		return self.request.process(self.routes['builds']['searchBuilds'], data, {'q': data['q']});

	def searchActiveEntitled(self, data = {}):
		return self.request.process(self.routes['builds']['searchActiveEntitled'], data, {'q': data['q']});

	def reindexBuilds(self):
		return self.request.process(self.routes['builds']['reindexBuilds']);

	def getBuildById(self, id):
		return self.request.process(self.routes['builds']['getBuildById'], {}, {'id': id});

	def createBuild(self, data = {}):
		return self.request.process(self.routes['builds']['createBuild'], data);

	def buildNow(self, data = {}):
		return self.request.process(self.routes['builds']['buildNow'], data);

	def updateBuildById(self, id, data = {}):
		return self.request.process(self.routes['builds']['updateBuildById'], data, {'id': id});

	def deleteBuildById(self, id):
		return self.request.process(self.routes['builds']['deleteBuildById'], {}, {'id': id});

	# Dockerservers
	def getDockerservers(self):
		return self.request.process(self.routes['dockerservers']['getDockerservers']);

	def getDockerserversManage(self, data = {}):
		return self.request.process(self.routes['dockerservers']['getDockerserversManage'], data);

	def getDockerserverById(self, id):
		return self.request.process(self.routes['dockerservers']['getDockerserverById'], {}, {'id': id});

	def getDockerserverStatusById(self, id):
		return self.request.process(self.routes['dockerservers']['getDockerserverStatusById'], {}, {'id': id});

	def getDockerserverPingById(self, id):
		return self.request.process(self.routes['dockerservers']['getDockerserverPingById'], {}, {'id': id});

	def createDockerserver(self, data = {}):
		return self.request.process(self.routes['dockerservers']['createDockerserver'], data);

	def updateDockerserverById(self, id, data = {}):
		return self.request.process(self.routes['dockerservers']['updateDockerserverById'], data, {'id': id});

	def deleteDockerserverById(self, id):
		return self.request.process(self.routes['dockerservers']['deleteDockerserverById'], {}, {'id': id});

	def searchDockerservers(self, data = {}):
		return self.request.process(self.routes['dockerservers']['searchDockerservers'], data, {'q': data['q']});

	def reindexDockerservers(self):
		return self.request.process(self.routes['dockerservers']['reindexDockerservers']);

	def monitorDockerserverById(self, id):
		return self.request.process(self.routes['dockerservers']['monitorDockerserverById'], {}, {'id': id});

	def getDockerserversManageById(self, id):
		return self.request.process(self.routes['dockerservers']['getDockerserversManageById'], {}, {'id': id});

	# Apps
	def getApps(self):
		return self.request.process(self.routes['apps']['getApps']);	

	def getAppById(self, id):
		return self.request.process(self.routes['apps']['getAppById'], {}, {'id': id});

	def getActiveApps(self, data = {}):
		return self.request.process(self.routes['apps']['getActiveApps'], data);

	def getDestroyedApps(self, data = {}):
		return self.request.process(self.routes['apps']['getDestroyedApps'], data);

	def deleteAllDestroyedApps(self):
		return self.request.process(self.routes['apps']['deleteAllDestroyedApps']);

	def updateAppById(self, id, data = {}):
		return self.request.process(self.routes['apps']['updateAppById'], data, {'id': id});

	def deployAppById(self, id):
		return self.request.process(self.routes['apps']['deployAppById'], {}, {'id': id});

	def getAppsDeploy(self):
		return self.request.process(self.routes['apps']['getAppsDeploy']);

	def stopAppById(self, id):
		return self.request.process(self.routes['apps']['stopAppById'], {}, {'id': id});

	def startAppById(self, id):
		return self.request.process(self.routes['apps']['startAppById'], {}, {'id': id});

	def restartAppById(self, id):
		return self.request.process(self.routes['apps']['restartAppById'], {}, {'id': id});

	def destroyAppById(self, id):
		return self.request.process(self.routes['apps']['destroyAppById'], {}, {'id': id});

	def getAppBackupsById(self, id):
		return self.request.process(self.routes['apps']['getAppBackupsById'], {}, {'id': id});

	def createAppBackupById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppBackupById'], data, {'id': id});

	def createAppBackupNowById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppBackupNowById'], data, {'id': id});

	def getAppPluginsById(self, id):
		return self.request.process(self.routes['apps']['getAppPluginsById'], {}, {'id': id});

	def createAppPluginById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppPluginById'], data, {'id': id});

	def createAppPluginNowById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppPluginNowById'], data, {'id': id});

	def appRollbackById(self, id):
		return self.request.process(self.routes['apps']['appRollbackById'], {}, {'id': id});

	def appRollbackNowById(self, id, data = {}):
		return self.request.process(self.routes['apps']['appRollbackNowById'], data, {'id': id});

	def createAppScaleOutCreateById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppScaleOutCreateById'], data, {'id': id});

	def getAppScaleInCreateById(self, id):
		return self.request.process(self.routes['apps']['getAppScaleInCreateById'], {}, {'id': id});

	def createAppScaleInById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppScaleInById'], data, {'id': id});

	def createAppScaleInNowById(self, id, data = {}):
		return self.request.process(self.routes['apps']['createAppScaleInNowById'], data, {'id': id});

	def searchApps(self, data = {}):
		return self.request.process(self.routes['apps']['searchApps'], data, {'q': data['q']});

	def appMonitorById(self, id):
		return self.request.process(self.routes['apps']['appMonitorById'], {}, {'id': id});

	# Usergroups
	def getUsergroups(self, data = {}):
		return self.request.process(self.routes['usergroups']['getUsergroups'], data);

	def getUsergroupById(self, id):
		return self.request.process(self.routes['usergroups']['getUsergroupById'], {}, {'id': id});

	def createUsergroup(self, data = {}):
		return self.request.process(self.routes['usergroups']['createUsergroup'], data);

	def updateUsergroupById(self, id, data = {}):
		return self.request.process(self.routes['usergroups']['updateUsergroupById'], data, {'id': id});

	def deleteUsergroupById(self, id):
		return self.request.process(self.routes['usergroups']['deleteUsergroupById'], {}, {'id': id});

	def searchUsergroups(self, data = {}):
		return self.request.process(self.routes['usergroups']['searchUsergroups'], data, {'q': data['q']});

	# Profiles
	def getProfiles(self, data = {}):
		return self.request.process(self.routes['profiles']['getProfiles'], data);

	def getProfileById(self, id):
		return self.request.process(self.routes['profiles']['getProfileById'], {}, {'id': id});

	def updateProfileById(self, id, data = {}):
		return self.request.process(self.routes['profiles']['updateProfileById'], data, {'id': id});

	def deleteProfileById(self, id, data = {}):
		return self.request.process(self.routes['profiles']['deleteProfileById'], data, {'id': id});

	def createProfile(self, data = {}):
		return self.request.process(self.routes['profiles']['createProfile'], data);

	def searchProfiles(self, data = {}):
		return self.request.process(self.routes['profiles']['searchProfiles'], data, {'q': data['q']});

	# Messages
	def searchMessages(self, data = {}):
		return self.request.process(self.routes['messages']['searchMessages'], data, {'q': data['q']});

	def getUnreadMessages(self, data = {}):
		return self.request.process(self.routes['messages']['getUnreadMessages'], data);

	def getOpenMessages(self, data = {}):
		return self.request.process(self.routes['messages']['getOpenMessages'], data);

	def getMessageById(self, id):
		return self.request.process(self.routes['messages']['getMessageById'], {}, {'id': id});

	def archiveMessageById(self, id):
		return self.request.process(self.routes['messages']['archiveMessageById'], {}, {'id': id});

	def getArchivedMessages(self, data = {}):
		return self.request.process(self.routes['messages']['getArchivedMessages'], data);

	def deleteMessageById(self, id):
		return self.request.process(self.routes['messages']['deleteMessageById'], {}, {'id': id});

	# Users
	def getUsers(self):
		return self.request.process(self.routes['users']['getUsers']);

	def getUserById(self, id):
		return self.request.process(self.routes['users']['getUserById'], {}, {'id': id});

	def updateUserById(self, id, data = {}):
		return self.request.process(self.routes['users']['updateUserById'], data, {'id': id});

	def deleteUserById(self, id):
		return self.request.process(self.routes['users']['deleteUserById'], {}, {'id': id});

	def createUser(self, data = {}):
		return self.request.process(self.routes['users']['createUser'], data);

	def searchUsers(self, data = {}):
		return self.request.process(self.routes['users']['searchUsers'], data, {'q': data['q']});

	def updateUserProfileById(self, id, data = {}):
		return self.request.process(self.routes['users']['updateUserProfileById'], data, {'id': id});

	def getUserLoginStatus(self):
		return self.request.process(self.routes['users']['getUserLoginStatus']);

	def signupUser(self, data = {}):
		return self.request.process(self.routes['users']['signupUser'], data);

	def signupTenantUser(self, data = {}):
		return self.request.process(self.routes['users']['signupTenantUser'], data);

	def searchUserByEmail(self, email):
		return self.request.process(self.routes['users']['searchUserByEmail'], {'email': email}, {'email': email});

	def generateUserPasswordResetByEmail(self, email):
		return self.request.process(self.routes['users']['generateUserPasswordResetByEmail'], {'email': email}, {'email': email});

	def resetUserPasswordResetById(self, id, password):
		return self.request.process(self.routes['users']['resetUserPasswordResetById'], {'newPassword': password}, {'id': id});

	# Plugins
	def createPlugin(self, data = {}):
		return self.request.process(self.routes['plugins']['createPlugin'], data);

	def getPluginsManage(self, data = {}):
		return self.request.process(self.routes['plugins']['getPluginsManage'], data);

	def getPluginManageById(self, id):
		return self.request.process(self.routes['plugins']['getPluginManageById'], {}, {'id': id});

	def getPluginsStarred(self, data = {}):
		return self.request.process(self.routes['plugins']['getPluginsStarred'], data);

	def updatePluginById(self, id, data = {}):
		return self.request.process(self.routes['plugins']['updatePluginById'], data, {'id': id});

	def deletePluginById(self, id):
		return self.request.process(self.routes['plugins']['deletePluginById'], {}, {'id': id});

	def searchPlugins(self, data = {}):
		return self.request.process(self.routes['plugins']['searchPlugins'], data, {'q': data['q']});

	def reindexPlugins(self):
		return self.request.process(self.routes['plugins']['reindexPlugins']);

	def searchActiveEntitledPlugins(self, data = {}):
		return self.request.process(self.routes['plugins']['searchActiveEntitledPlugins'], data, {'q': data['q']});

	def starPluginById(self, id):
		return self.request.process(self.routes['plugins']['starPluginById'], {}, {'id': id});

	def unstarPluginById(self, id):
		return self.request.process(self.routes['plugins']['unstarPluginById'], {}, {'id': id});

	def getPlugins(self, data = {}):
		return self.request.process(self.routes['plugins']['getPlugins'], data);

	# Cloudproviders
	def getCloudproviderRegionsById(self, id):
		return self.request.process(self.routes['cloudproviders']['getCloudproviderRegionsById'], {}, {'id': id});

	def getCloudproviderMachinetypesById(self, id, data = {}):
		return self.request.process(self.routes['cloudproviders']['getCloudproviderMachinetypesById'], data, {'id': id});

	def getCloudproviderMachineimagesByIdRegion(self, id, region = '', data = {}):
		return self.request.process(self.routes['cloudproviders']['getCloudproviderMachineimagesByIdRegion'], data, {'id': id, 'region': region});

	def getCloudproviderNetworksByIdRegion(self, id, region = '', data = {}):
		return self.request.process(self.routes['cloudproviders']['getCloudproviderNetworksByIdRegion'], data, {'id': id, 'region': region});

	def getCloudproviderSecuritygroupsByIdRegion(self, id, region = '', data = {}):
		return self.request.process(self.routes['cloudproviders']['getCloudproviderSecuritygroupsByIdRegion'], data, {'id': id, 'region': region});

	# Registryaccounts
	def getRegistryaccounts(self):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccounts']);

	def getRegistryaccountById(self, id):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccountById'], {}, {'id': id});

	def deleteRegistryaccountById(self, id):
		return self.request.process(self.routes['registryaccounts']['deleteRegistryaccountById'], {}, {'id': id});

	def getRegistryaccountsManage(self, data = {}):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccountsManage'], data);

	def searchRegistryaccounts(self, data = {}):
		return self.request.process(self.routes['registryaccounts']['searchRegistryaccounts'], data, {'q': data['q']});

	def reindexRegistryaccounts(self):
		return self.request.process(self.routes['registryaccounts']['reindexRegistryaccounts']);

	def getRegistryaccountJenkinsById(self, id):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccountJenkinsById'], {}, {'id': id});

	def getRegistryaccountTypeById(self, id):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccountTypeById'], {}, {'id': id});

	def getRegistryaccountCloudproviders(self):
		return self.request.process(self.routes['registryaccounts']['getRegistryaccountCloudproviders']);

	def createRegistryaccount(self, data = {}):
		return self.request.process(self.routes['registryaccounts']['createRegistryaccount'], data);

	def updateRegistryaccountById(self, id, data = {}):
		return self.request.process(self.routes['registryaccounts']['updateRegistryaccountById'], data, {'id': id});

	# Settings
	def settingsEncrypt(self, key = '', text = ''):
		return self.request.process(self.routes['settings']['settingsEncrypt'], {'key': key, 'text': text}, {'key': key, 'text': text});

	def settingsRecreateMissingQueues(self):
		return self.request.process(self.routes['settings']['settingsRecreateMissingQueues']);
