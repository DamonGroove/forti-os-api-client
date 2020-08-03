from simple_rest_client.resource import Resource


class UTMMonitor(Resource):
    actions = {
        "rating_lookup": {"method": "GET", "url": "/utm/rating-lookup/select{}"}
    }
