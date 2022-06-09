import requests

# register a user
USER_NAME = "littlejixi520"
TOKEN = "ghtfrhgfndknokygrgsfdvj"
pixe_endpoint = "https://pixe.la/v1/users"
user_para = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
response = requests.post(url=pixe_endpoint, json=user_para)
response.raise_for_status()
print(response.text)


# create a graph
# graph_endpoint = f"{pixe_endpoint}/{USER_NAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# graph_config = {
#     "id": "my1graph",
#     "name": "python",
#     "unit": "hour",
#     "type": "float",
#     "color": "sora",
#     "timezone": "Asia/China"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# data = response.text
# print(data)
