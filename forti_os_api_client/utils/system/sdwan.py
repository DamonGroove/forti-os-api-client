from forti_os_api_client.rest.client import fortigate_api_cmdb
from forti_os_api_client.rest.resources.cmdb.system import SystemCMDB



class SDWan:
    # Define resources
    fortigate_api_cmdb.add_resource(resource_name="system", resource_class=SystemCMDB)

    # Configure SDWAN
