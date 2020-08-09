from RestResponse import RestResponse

from forti_os_api_client.csv.csv_processor import CSVProcessor
from forti_os_api_client.rest.client import fortigate_api_monitor
from forti_os_api_client.rest.resources.monitor.utm import UTMMonitor


class FortiGuardRating:
    # Define resources
    fortigate_api_monitor.add_resource(resource_name="utm", resource_class=UTMMonitor)

    def __init__(self, category_column='fortigate category', subcategory_column='fortigate subcategory', url_column='url'):
        self.category_column = category_column
        self.subcategory_column = subcategory_column
        self.web_category_columns = {category_column, subcategory_column}
        self.url_column = url_column

    @staticmethod
    def lookup(url):
        results = RestResponse.parse(fortigate_api_monitor.utm.rating_lookup("?url={}".format(url)).body).results
        if results.subcategory == 'Unrated':
            return ['Unrated', results.subcategory]
        return [results.category, results.subcategory]

    def get_list(self, src_csv_path):
        processor = CSVProcessor()
        row_list = processor.read(src_csv_path)
        ratings_list = []
        for row in row_list:
            rating = self.lookup(row.get(self.url_column))
            row[self.category_column] = rating[0]
            row[self.subcategory_column] = rating[1]
            ratings_list.append(row)
        return ratings_list

    def write_csv(self, src_csv_path, out_csv_path):
        processor = CSVProcessor()
        processor.write_func(processor.read(src_csv_path), out_csv_path, self.web_category_columns, self.lookup,
                             self.url_column)

