from RestResponse import RestResponse


# If table is being used a blank query needs to be in place, sometimes . e.g. table("")
# table parameter e.g. fortigate_api_cmdb.system.interfaces
# body parameter e.g. {"status": "enable"}; Use getObject(table) to get usable parameters


# Get the QType from a CMDB table
def get_q_type(table):
    return RestResponse.parse(table("?action=schema").body).results.q_type


class QType:
    # Table as a parameter
    # Get the QType from a CMDB table
    @staticmethod
    def get(table):
        return RestResponse.parse(table("?action=schema").body).results.q_type
