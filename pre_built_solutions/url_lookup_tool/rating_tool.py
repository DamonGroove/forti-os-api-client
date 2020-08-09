from forti_os_api_client.csv.csv_processor import CSVProcessor
from forti_os_api_client.utils.webfiltering.local_category import LocalCategory
from forti_os_api_client.utils.webfiltering.local_rating import LocalRating
from forti_os_api_client.utils.webfiltering.fortiguard_rating import FortiGuardRating
from forti_os_api_client.utils.webfiltering.web_profile import WebProfile


class RatingTool:

    def __init__(self, import_csv):
        self.fortiguard_rating = FortiGuardRating()
        self.ratingsList = self.fortiguard_rating.get_list(import_csv)

    # Return a list of URLs that are not blocked by a FortiGate's web filtering profile, but should be blocked
    def to_deny_url_list(self, url_list, non_fgt_allow_cat, non_fgt_cat_col, fgt_cat_col, url_col, fgt_web_profile):
        profile = WebProfile()
        to_deny_list = []
        denied_cats = profile.get_denied_categories(fgt_web_profile)
        # print(len(url_list))
        # print(denied_cats)
        for row in url_list:
            if non_fgt_allow_cat != row.get(non_fgt_cat_col):
                is_fgt_cat_denied = self.__is_fgt_denied(row.get(fgt_cat_col), denied_cats)
                if not is_fgt_cat_denied:
                    to_deny_list.append(row.get(url_col))

        return to_deny_list

    # Return a list of Categories that are not blocked by a FortiGate's web filtering profile, but should be blocked
    def to_deny_cat_list(self, url_list, non_fgt_allow_cat, non_fgt_cat_col, fgt_cat_col, fgt_web_profile):
        profile = WebProfile()
        to_deny_list = []
        denied_cats = profile.get_denied_categories(fgt_web_profile)

        # Check if list items are blocked, otherwise add to to_deny_list
        for row in url_list:
            if non_fgt_allow_cat != row.get(non_fgt_cat_col):
                is_fgt_cat_denied = self.__is_fgt_denied(row.get(fgt_cat_col), denied_cats)
                if not is_fgt_cat_denied:
                    fgt_cat = row.get(fgt_cat_col)
                    if not self.__has_item(fgt_cat, to_deny_list):
                        to_deny_list.append(fgt_cat)

        return to_deny_list

    # Return a list of blocked/denied URLs and their Categories and Sub-Categories
    def get_deny_url_cat(self, url_list):
        # print(len(url_list))
        cat_url_list = []
        for url in url_list:
            category = self.fortiguard_rating.lookup(url)
            category.append(url)
            cat_url_list.append(category)
        # print(len(cat_url_list))
        return cat_url_list

    # Check if the fgt_cat is is in the denied_cats list
    @staticmethod
    def __is_fgt_denied(fgt_cat, denied_cats):
        for cat in denied_cats:
            if cat == fgt_cat:
                return True
        return False

    # Check if a list already contains an item
    @staticmethod
    def __has_item(item, item_list):
        for obj in item_list:
            if obj == item:
                return True
        return False

    # Import local ratings and categories
    def import_ratings(self, items):
        local_rating = LocalRating()
        local_category = LocalCategory()
        clean_list = []
        for item in items:
            clean_url = self.__cleanup_url(item[2])
            # print(clean_url, rating)
            custom_name = "custom_{}".format(item[1])
            if not self.__has_local_cat(custom_name, local_category.get_list()):
                local_category.post(custom_name)
            if not self.__has_rating(clean_url, local_rating.get()):
                local_rating.post(clean_url, local_category.get(custom_name).id)
                print(clean_url)
                clean_list.append(clean_url)
        # print("Ratings from FortiGate: ", len(local_rating.get()))
        # print("Ratings from array: ", len(clean_list))

        return local_rating.get()

    @staticmethod
    def __has_local_cat(item, item_list):
        for obj in item_list:
            if obj.desc == item:
                return True
        return False

    @staticmethod
    def __has_rating(item, item_list):
        for obj in item_list:
            if obj.url == item:
                return True
        return False

    @staticmethod
    def __cleanup_url(url):
        url_changed = False

        if "*." in url:
            param, clean_url = url.split("*.", 1)
            url_changed = True
        elif "://" in url:
            param, clean_url = url.split("://", 1)
            url_changed = True
        if not url_changed:
            clean_url = url
        if "*" and clean_url.endswith("*"):
            return clean_url[:-len("*")]

        return clean_url


# Export a CSV of a URL's category and subcategory that needs to blocked
# Example Use:
rating_tool = RatingTool("import_web_filter.csv")
# csv_processor = CSVProcessor()
# csv_processor.write(rating_tool.get_deny_url_cat(rating_tool.to_deny_url_list(rating_tool.ratingsList, "la",
#                                      "external category", "fortigate subcategory", "url", "test3")), "export.csv")
#
rating_tool.import_ratings(rating_tool.get_deny_url_cat(rating_tool.to_deny_url_list(rating_tool.ratingsList, "la",
                                                 "external category", "fortigate subcategory", "url", "test3")))
