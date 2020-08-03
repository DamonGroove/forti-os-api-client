from simple_rest_client.resource import Resource


class SystemMonitor(Resource):
    actions = {
        "object_usage": {"method": "GET", "url": "/system/object/usage{}"}
    }