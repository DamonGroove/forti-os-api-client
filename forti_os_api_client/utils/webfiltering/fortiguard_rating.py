from RestResponse import RestResponse

from forti_os_api_client.csv.csv_processor import CSVProcessor
from forti_os_api_client.rest.client import fortigate_api_monitor
from forti_os_api_client.rest.resources.monitor.utm import UTMMonitor


class FortiGuardRating:
    # Define resources
    fortigate_api_monitor.add_resource(resource_name="utm", resource_class=UTMMonitor)

    web_category_columns = {'fortigate category', 'fortigate subcategory'}
    url_column = 'url'

    @classmethod
    def lookup(cls, url):
        results = RestResponse.parse(fortigate_api_monitor.utm.rating_lookup("?url={}".format(url)).body).results
        if results.subcategory == 'Unrated':
            return ['Unrated', results.subcategory]
        return [results.category, results.subcategory]

    @classmethod
    def get_list(cls, src_csv_path):
        processor = CSVProcessor()
        row_list = processor.read(src_csv_path)
        ratings_list = []
        for row in row_list:
            rating = cls.lookup(row.get(cls.url_column))
            row['fortigate category'] = rating[0]
            row['fortigate subcategory'] = rating[1]
            ratings_list.append(row)
        return ratings_list

    @classmethod
    def write_csv(cls, src_csv_path, out_csv_path):
        processor = CSVProcessor()
        processor.write_func(processor.read(src_csv_path), out_csv_path, cls.web_category_columns, cls.lookup,
                             cls.url_column)

