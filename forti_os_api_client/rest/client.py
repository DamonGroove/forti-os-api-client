import socket

from simple_rest_client.api import API
from settings import fgt_token, fgt_ip

# Get fgt_token environment variable from settings.py
token = fgt_token

# Get fgt_ip environment variable from settings.py
fortigate_name = socket.gethostbyaddr(fgt_ip)[0]
# Resolve FortiGate's name
default_params = {"access_token": "{}".format(token)}

# Define CMDB API
fortigate_api_cmdb = API(
    api_root_url="https://{}/api/v2/cmdb".format(fortigate_name),
    params=default_params,
    json_encode_body=True,
    ssl_verify=False
)

# Define Monitor API
fortigate_api_monitor = API(
    api_root_url="https://{}/api/v2/monitor".format(fortigate_name),
    params=default_params,
    json_encode_body=True,
    ssl_verify=False
)


