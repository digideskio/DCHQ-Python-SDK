from dchq.dchq import Dchq
d=Dchq({'username':'admin@dchq.io','password':'admin123'})


print d.getBlueprints()
'''
print d.createBlueprint({
"name": "amal-Nginx-test",
"blueprintType": "DOCKER_COMPOSE",
"version": "2.0",
"yml": ""
});
print d.getBlueprintsManage();
print d.getBlueprintsManageById('4028818650d4aca10150d4bf63470003');
print d.searchBlueprintsLibraryPage({'q': 'amal'});
print d.getBlueprintById('2c91808651a95c4d0151da0e9b087679');
print d.updateBlueprintById('2c91808651a95c4d0151da0e9b087679', {
	'description': 'Created by amal for testing',
	'name': 'amal-Nginx-test-again-again',
	"blueprintType": "DOCKER_COMPOSE",
	"version": "2.0",
	"yml": ""
});
print d.deleteBlueprintById('2c91808651a95c4d0151da0e9b087679');
print d.starBlueprintById('2c91808651a95c4d0151da0e9b087679');
print d.unstarBlueprintById('2c91808651a95c4d0151da0e9b087679');
print d.getStarredBlueprints();
print d.getBlueprintYamlById('402881864e1a36cc014e1a399cf90101');

print d.getDatacenters();
print d.getDatacenterById('2c91808651a95c4d0151c4cfabf21cb3');
print d.createDatacenter({
	'name': 'amal-test-datacenter'
});
print d.updateDatacenterById('2c91808651a95c4d0151dc98f37a0548', {
	'name': 'amal-test-datacenter-edited-python'
});
print d.deleteDatacenterById('2c91808651a95c4d0151c4cfabf21cb3');
print d.getDatacentersManage();
print d.searchDatacenters({'q': 'amal'});

print d.getBuilds();
print d.getBuildsManage();
print d.getBuildsManageById('addsaf');
print d.searchBuilds({'q': 'amal'});
print d.searchActiveEntitled({'q': 'amal'});
print d.reindexBuilds();
print d.getBuildById('adsa');
print d.createBuild({'name': 'amal-test-build', 'repository': 'dsfs', 'tag': 'test'});
print d.buildNow({'name': 'amal-test-build', 'repository': 'dsfs', 'tag': 'test'});
print d.updateBuildById('adsfdsf', {'name': 'amal-test-build-edited', 'repository': 'dsfs', 'tag': 'test'});
print d.deleteBuildById('sdkfmk');

print d.getDockerservers();
print d.getDockerserversManage();
print d.getDockerserverById('asda');
print d.getDockerserverStatusById('asda');
print d.getDockerserverPingById('asda');
print d.createDockerserver({
    "name": "kjwdnfkjs",
    "hostOrIp": "akjnf",
    "description": "lnsdknfkl",
    "size": 1,
    "inactive": False,
    "dataCenter": {}
});;
print d.updateDockerserverById('asdasdhj', {
    "name": "kjwdnfkjs",
    "hostOrIp": "akjnf",
    "description": "lnsdknfkl",
    "inactive": False
});
print d.deleteDockerserverById('asda');

print d.getApps();
print d.getAppById('dsafds');
print d.getActiveApps();
print d.getDestroyedApps();
print d.deleteAllDestroyedApps();
print d.updateAppById('adas', {});
print d.deployAppById('dsafds');
print d.getAppsDeploy();
print d.stopAppById('sdfs');
print d.startAppById('sdfs');
print d.restartAppById('sdfs');
print d.destroyAppById('sdfds');
print d.getAppBackupsById('dfsfd');
print d.createAppBackupById('sgffd');
print d.getAppPluginsById('fsdf');
print d.createAppPluginById('sdfs', {'continuous': True, 'note': 'aaf'});
print d.createAppPluginNowById('sdfs', {'continuous': True, 'note': 'aaf'});
print d.appRollbackById('dsfs');
print d.appRollbackNowById('sdfs', {'continuous': True, 'note': 'aaf'});
print d.createAppScaleOutCreateById('sdfs');
print d.getAppScaleInCreateById('sdfs');
print d.createAppScaleInById('sdfs');
print d.createAppScaleInNowById('sdfsdf');
print d.searchApps({'q': 'sadfdsf'});
print d.appMonitorById('adsas');

print d.getUsergroups();
print d.getUsergroupById('2c91808651a95c4d0151ea023320555b');
print d.createUsergroup({'name': 'sadfdsf'});
print d.updateUsergroupById('2c91808651a95c4d0151ea023320555b', {'name': 'amal'});
print d.deleteUsergroupById('2c91808651a95c4d0151ea023320555b');
print d.searchUsergroups({'q': 'sadfdsf'});

print d.getProfiles();
print d.getProfileById('dsgfdg');
print d.updateProfileById('dsgfdg', {'name': 'amal'});
print d.deleteProfileById('dsgfdg');
print d.createProfile({'name': 'amal', 'defaultProfile': True});
print d.searchProfiles({'q': 'amal'});

print d.searchMessages({'q': 'amal'});
print d.getUnreadMessages();
print d.getOpenMessages();
print d.getMessageById('sfds');
print d.archiveMessageById('sfds');
print d.getArchivedMessages();
print d.deleteMessageById('sdfsdf');

print d.getUsers();
print d.getUserById('dsfds');
print d.updateUserById('sfds', {
	'firstname': 'dfsdf'
});
print d.deleteUserById('dsfsd');
print d.createUser({
    "username": "amal-test",
    "password": "password",
    "email": "amal@amal.com",
    "firstname": "amal",
    "lastname": "francis",
    "enabled": True,
    "company": "amal",
    "jobTitle": "amal",
    "phoneNumber": "1234567890"
});
print d.searchUsers({'q': 'amal'});
print d.updateUserProfileById('2c91808651a95c4d0151f2c0aaa611d9', {
    "company": "amal company"
});
print d.getUserLoginStatus();
print d.signupUser({
    "username": "amal-test",
    "password": "password",
    "email": "amal@amal.com",
    "firstname": "amal",
    "lastname": "francis",
    "company": "amal"
});
print d.signupTenantUser({
    "username": "amal-test",
    "password": "password",
    "email": "amal@amal.com",
    "firstname": "amal",
    "lastname": "francis",
    "company": "amal"
});
print d.searchUserByEmail('amalfra@gmail.com');
print d.generateUserPasswordResetByEmail('amalfra@gmail.com');
print d.resetUserPasswordResetById('hjsdfhd', 'password');

print d.createPlugin({
    "name": "amal-test",
    "version": "1.0",
    "license": "MIT",
    "description": "amal test",
		"baseScript": 'test'
});
print d.getPluginsManage();
print d.getPluginManageById('safd');
print d.getPluginsStarred();
print d.updatePluginById('2c91808651a95c4d0151f318c64f1444', {
    "name": "amal-test updated"
});
print d.deletePluginById('2c91808651a95c4d0151f318c64f1444');
print d.searchPlugins({'q': 'amal'});
print d.reindexPlugins();
print d.searchActiveEntitledPlugins({'q': 'amal'});
print d.starPluginById('2c91808651a95c4d0151f318c64f1444');
print d.unstarPluginById('2c91808651a95c4d0151f318c64f1444');
print d.getPlugins();

print d.getCloudproviderRegionsById('fsd');
print d.getCloudproviderMachinetypesById('sdkjfn');
print d.getCloudproviderMachineimagesByIdRegion('sdkjfn', 'sadfdsf');
print d.getCloudproviderNetworksByIdRegion('sdkjfn', 'sadfdsf');
print d.getCloudproviderSecuritygroupsByIdRegion('sdkjfn', 'sadfdsf');

print d.getRegistryaccounts();
print d.getRegistryaccountById('asda');
print d.deleteRegistryaccountById('asda');
print d.getRegistryaccountsManage();
print d.searchRegistryaccounts({'q': 'amal'});
print d.reindexRegistryaccounts();
print d.getRegistryaccountJenkinsById('dsfsdf');
print d.getRegistryaccountTypeById('sdgdf');
print d.getRegistryaccountCloudproviders();
print d.createRegistryaccount({'name': 'amal-test'});
print d.updateRegistryaccountById('2c91808651a95c4d0151f7398ab92c80', 
	{'name': 'amal-test renamed'});

print d.settingsEncrypt('dsfdsf', 'sdfdsf');'''
print d.settingsRecreateMissingQueues();
