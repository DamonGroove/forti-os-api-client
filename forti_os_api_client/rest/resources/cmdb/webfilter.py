from simple_rest_client.resource import Resource


class WebfilterCMDB(Resource):
    actions = {
        "profile": {"method": "GET", "url": "/webfilter/profile/{}"}
    }
