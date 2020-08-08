from simple_rest_client.resource import Resource


class WebfilterCMDB(Resource):
    actions = {
        "profile": {"method": "GET", "url": "/webfilter/profile/{}"},
        "ftgd_local_cats": {"method": "GET", "url": "/webfilter/ftgd-local-cat"},
        "ftgd_local_cat": {"method": "GET", "url": "/webfilter/ftgd-local-cat/{}"},
        "new_ftgd_local_cat": {"method": "POST", "url": "/webfilter/ftgd-local-cat"},
        "ftgd_local_ratings": {"method": "GET", "url": "/webfilter/ftgd-local-rating"},
        "new_ftgd_local_rating": {"method": "POST", "url": "/webfilter/ftgd-local-rating"},
    }
