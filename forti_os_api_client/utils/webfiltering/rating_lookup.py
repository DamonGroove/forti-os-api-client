from RestResponse import RestResponse

from forti_os_api_client.csv.csv_processor import write_csv_with_function, read_csv
from forti_os_api_client.rest.client import fortigate_api_monitor
from forti_os_api_client.rest.resources.monitor.utm import UTMMonitor

# Define resources
fortigate_api_monitor.add_resource(resource_name="utm", resource_class=UTMMonitor)

web_category_columns = {'fortigate category', 'fortigate subcategory'}
url_column = 'url'


def rating_lookup(url):
    results = RestResponse.parse(fortigate_api_monitor.utm.rating_lookup("?url={}".format(url)).body).results
    return [results.category, results.subcategory]


def get_ratings_list(src_csv_path):
    row_list = read_csv(src_csv_path)
    ratings_list = []
    for row in row_list:
        rating = rating_lookup(row.get(url_column))
        count = 0
        for name in web_category_columns:
            row[name] = rating[count]
            count = count + 1
        ratings_list.append(row)
    return ratings_list


def write_ratings_to_csv(src_csv_path, out_csv_path):
    write_csv_with_function(read_csv(src_csv_path), out_csv_path, web_category_columns, rating_lookup, url_column)

