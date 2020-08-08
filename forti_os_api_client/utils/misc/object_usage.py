# Put object with the table and body as parameters
from RestResponse import RestResponse

from forti_os_api_client.rest.client import fortigate_api_monitor, fortigate_api_cmdb
from forti_os_api_client.rest.resources.cmdb.system import SystemCMDB
from forti_os_api_client.rest.resources.cmdb.webfilter import WebfilterCMDB
from forti_os_api_client.rest.resources.monitor.system import SystemMonitor
from forti_os_api_client.utils.misc.q_type import QType


class ObjectUsage:
    # Define resources
    fortigate_api_cmdb.add_resource(resource_name="system", resource_class=SystemCMDB)
    fortigate_api_cmdb.add_resource(resource_name="webfilter", resource_class=WebfilterCMDB)
    fortigate_api_monitor.add_resource(resource_name="system", resource_class=SystemMonitor)

    # List table's objects and their use count
    @staticmethod
    def get_list(table):
        return [[obj.name, len(table.get(obj.name, table))] for obj in RestResponse.parse(table("").body).results]

    # Get object's use
    @staticmethod
    def get(obj, table):
        q_type = QType()

        return RestResponse.parse(fortigate_api_monitor.system.object_usage(
            "?mkey={}&qtypes=%5B{}%5D".format(obj, q_type.get(table))).body).results.currently_using


# Example Use:
# usage = ObjectUsage
# print(usage.get("wan1", fortigate_api_cmdb.system.interfaces))
