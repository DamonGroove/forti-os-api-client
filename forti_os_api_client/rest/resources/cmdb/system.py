from simple_rest_client.resource import Resource


class SystemCMDB(Resource):
    actions = {
        "dns": {"method": "GET", "url": "/system/dns{}"},
        "new_dns": {"method": "PUT", "url": "/system/dns"},
        "interfaces": {"method": "GET", "url": "/system/interface{}"},
        "interface": {"method": "GET", "url": "/system/interface/{}"},
        "virtual_wan_link": {"method": "GET", "url": "/system/virtual-wan-link{}"},
        "new_virtual_wan_link": {"method": "PUT", "url": "/system/virtual-wan-link"}
    }