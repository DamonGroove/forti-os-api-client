forti-os-api-client

A Useful FortiOS API Client Library

Getting Started:

- Clone the Repository
- cd to project_name
- run: pip install simple-rest-client
- run: pip install -U python-dotenv
- create a .env file
- Set environment variables, matching the variables under /settings.py
- Create a REST API administrator within FortiOS with the appropriate permissions and trusted hosts
- Generate an auth token for the administrator
- Add the FortiGate's auth token and IP address to the .env
- Make sure you can resolve the IP address to the FortiGate's hostname
- Build new solutions with the modules under /utils or use prebuilt solutions under /pre_built_solutions

Usage:

Utilize prebuilt modules and solutions to automate FortiOS's functionality.

Any requests for prebuilt solutions are welcome.
