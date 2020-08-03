from simple_rest_client.resource import Resource


class WebfilterMonitor(Resource):
    actions = {
        "fortiguard_categories": {"method": "GET", "url": "/webfilter/fortiguard-categories"}
    }
