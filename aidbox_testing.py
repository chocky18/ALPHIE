# # import requests

# # url = "http://localhost:8080/fhir/Patient"
# # headers = {
   
# #     "Content-Type": "text/yaml",
# #     "Accept": "text/yaml"
# # }

# # data = """
# # id: pt-1
# # name:
# #   - family: "John"
# # """

# # response = requests.post(url, headers=headers, data=data)

# # print(response.text)

# import os
# import requests

# # Read login details from environment variables
# AIDBOX_USERNAME = os.getenv("AIDBOX_USERNAME")  # Your Aidbox username
# AIDBOX_PASSWORD = os.getenv("AIDBOX_PASSWORD")  # Your Aidbox password
# AIDBOX_URL = "http://localhost:8080/fhir/Patient"  # Adjust URL if needed

# # Set headers for authentication using Basic Auth
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# # Patient data to send
# data = {
#     "resourceType": "Patient",
#     "id": "pt-1",
#     "name": [{"family": "John"}]
# }

# # Send request with Basic Authentication
# response = requests.post(AIDBOX_URL, json=data, headers=headers, auth=(AIDBOX_USERNAME, AIDBOX_PASSWORD))

# # Print response
# print(response.status_code, response.json())
import requests
import os

AIDBOX_USERNAME = os.getenv("AIDBOX_USERNAME")  # Admin username
AIDBOX_PASSWORD = os.getenv("AIDBOX_PASSWORD")  # Admin password
AIDBOX_URL = "http://localhost:8080/User/TinnaluriNaresh"

headers = {
    "Accept": "text/yaml",
    "Content-Type": "text/yaml"
}

data = """
password: 'Naruto@18'
data:
  name: Tinnaluri Naresh
  roles:
    - Developer
"""

response = requests.put(AIDBOX_URL, headers=headers, data=data, auth=(AIDBOX_USERNAME, AIDBOX_PASSWORD))

print(response.status_code, response.text)
