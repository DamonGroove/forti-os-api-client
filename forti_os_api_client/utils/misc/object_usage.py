# Put object with the table and body as parameters
from RestResponse import RestResponse

from forti_os_api_client.rest.client import fortigate_api_monitor, fortigate_api_cmdb
from forti_os_api_client.rest.resources.cmdb.system import SystemCMDB
from forti_os_api_client.rest.resources.cmdb.webfilter import WebfilterCMDB
from forti_os_api_client.rest.resources.monitor.system import SystemMonitor
from forti_os_api_client.utils.misc.q_type import get_q_type


# Define resources
fortigate_api_cmdb.add_resource(resource_name="system", resource_class=SystemCMDB)
fortigate_api_cmdb.add_resource(resource_name="webfilter", resource_class=WebfilterCMDB)
fortigate_api_monitor.add_resource(resource_name="system", resource_class=SystemMonitor)


# List table's objects and their use count
def list_objects_use_count(table):
    return [[obj.name, len(get_object_use(obj.name, table))] for obj in RestResponse.parse(table("").body).results]


# Get object's use
def get_object_use(obj, table):
    return RestResponse.parse(fortigate_api_monitor.system.object_usage(
        "?mkey={}&qtypes=%5B{}%5D".format(obj, get_q_type(table))).body).results.currently_using

# Example use:
# print(getObjectUse("monitor-all", fortigate_api_cmdb.webfilter.profile))
# print(getObjectUse("wan1", fortigate_api_cmdb.system.interfaces))
# print(listObjectsUseCount(fortigate_api_cmdb.system.interfaces))
