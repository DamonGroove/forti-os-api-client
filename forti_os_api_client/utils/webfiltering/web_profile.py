from RestResponse import RestResponse

from forti_os_api_client.rest.client import fortigate_api_cmdb, fortigate_api_monitor
from forti_os_api_client.rest.resources.cmdb.webfilter import WebfilterCMDB
from forti_os_api_client.rest.resources.monitor.webfilter import WebfilterMonitor


class WebProfile:
    fortigate_api_cmdb.add_resource(resource_name="webfilter", resource_class=WebfilterCMDB)
    fortigate_api_monitor.add_resource(resource_name="webfilter", resource_class=WebfilterMonitor)

    # Get a list of denied categories from a web filter profile
    @classmethod
    def get_denied_categories(cls, profile):
        results = RestResponse.parse(fortigate_api_cmdb.webfilter.profile(profile).body).results
        deny_list = []

        for obj in results[0]["ftgd-wf"]["filters"]:
            if obj["action"] == "block":
                deny_list.append(cls.__get_cat_name(obj["category"]))
        return deny_list

    # Get a Category's name with its ID
    @classmethod
    def __get_cat_name(cls, cat_id):
        results = RestResponse.parse(fortigate_api_monitor.webfilter.fortiguard_categories().body).results
        name = ""
        hasMatchingID = False

        for obj in results:
            if cat_id == obj["id"]:
                name = obj["name"]
                hasMatchingID = True
            elif cat_id == 0:
                name = "Unrated"
                hasMatchingID = True

        if not hasMatchingID:
            print("Missing ID: ", cat_id)

        return name
