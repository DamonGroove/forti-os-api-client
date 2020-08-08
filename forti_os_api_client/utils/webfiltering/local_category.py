import logging

from RestResponse import RestResponse

from forti_os_api_client.rest.client import fortigate_api_cmdb
from forti_os_api_client.rest.resources.cmdb.webfilter import WebfilterCMDB

logger = logging.getLogger(__name__)


class LocalCategory:
    fortigate_api_cmdb.add_resource(resource_name="webfilter", resource_class=WebfilterCMDB)

    @staticmethod
    def get_list():
        results = RestResponse.parse(fortigate_api_cmdb.webfilter.ftgd_local_cats().body).results
        return results

    @staticmethod
    def get(local_cat):
        results = RestResponse.parse(fortigate_api_cmdb.webfilter.ftgd_local_cat(local_cat).body).results
        return results[0]

    @staticmethod
    def post(local_cat):
        response = RestResponse.parse(fortigate_api_cmdb.webfilter.new_ftgd_local_cat(body={"desc": local_cat}))
        return response.status_code == 200

