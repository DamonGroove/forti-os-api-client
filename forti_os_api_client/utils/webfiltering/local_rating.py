import logging

from RestResponse import RestResponse

from forti_os_api_client.rest.client import fortigate_api_cmdb
from forti_os_api_client.rest.resources.cmdb.webfilter import WebfilterCMDB

logger = logging.getLogger(__name__)


class LocalRating:
    fortigate_api_cmdb.add_resource(resource_name="webfilter", resource_class=WebfilterCMDB)

    @staticmethod
    def get():
        results = RestResponse.parse(fortigate_api_cmdb.webfilter.ftgd_local_ratings().body).results
        return results

    @staticmethod
    def post(url, cat_id):
        response = RestResponse.parse(
            fortigate_api_cmdb.webfilter.new_ftgd_local_rating(body={"url": url, "rating": cat_id}))
        return response.status_code == 200
