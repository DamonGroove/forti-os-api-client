from forti_os_api_client.csv.csv_processor import write_csv
from forti_os_api_client.utils.webfiltering.rating_lookup import get_ratings_list, rating_lookup
from forti_os_api_client.utils.webfiltering.web_profile import get_denied_categories

# Define File paths
import_file = 'import_web_filter.csv'
export_file = 'export.csv'
# Output ratings list by processing csv import
ratingsList = get_ratings_list(import_file)


# Return a list of URLs that are not blocked by a FortiGate's web filtering profile, but should be blocked
def to_deny_url_list(url_list, non_fgt_allow_cat, non_fgt_cat_col, fgt_cat_col, url_col, fgt_web_profile):
    to_deny_list = []
    denied_cats = get_denied_categories(fgt_web_profile)
    for row in url_list:
        if non_fgt_allow_cat != row.get(non_fgt_cat_col):
            is_fgt_cat_denied = is_fgt_denied(row.get(fgt_cat_col), denied_cats)
            if not is_fgt_cat_denied:
                to_deny_list.append(row.get(url_col))

    return to_deny_list


# Return a list of Categories that are not blocked by a FortiGate's web filtering profile, but should be blocked
def to_deny_cat_list(url_list, non_fgt_allow_cat, non_fgt_cat_col, fgt_cat_col, fgt_web_profile):
    to_deny_list = []
    denied_cats = get_denied_categories(fgt_web_profile)

    # Check if list items are blocked, otherwise add to to_deny_list
    for row in url_list:
        if non_fgt_allow_cat != row.get(non_fgt_cat_col):
            is_fgt_cat_denied = is_fgt_denied(row.get(fgt_cat_col), denied_cats)
            if not is_fgt_cat_denied:
                fgt_cat = row.get(fgt_cat_col)
                if not has_item(fgt_cat, to_deny_list):
                    to_deny_list.append(fgt_cat)

    return to_deny_list


# Return a list of blocked/denied URLs and their Categories and Sub-Categories
def get_deny_url_cat(url_list):
    cat_url_list = []
    short_cat_list = []
    for url in url_list:
        category = rating_lookup(url)
        short_cat_list.append(category[1])
        category.append(url)
        cat_url_list.append(category)

    return cat_url_list


# Check if the fgt_cat is is in the denied_cats list
def is_fgt_denied(fgt_cat, denied_cats):
    for cat in denied_cats:
        if cat == fgt_cat:
            return True
    return False


# Check if a list already contains an item
def has_item(item, item_list):
    for obj in item_list:
        if obj == item:
            return True
    return False


# Export a CSV of a URL's category and subcategory that needs to blocked
write_csv(get_deny_url_cat(to_deny_url_list(ratingsList, "la",
                                     "external category", "fortigate subcategory", "url", "test1")), export_file)
