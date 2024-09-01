import requests
from secret import USER_NAME, TOKEN
import datetime as dt

today = dt.datetime.today().strftime(format="%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_post_params = {
    "date": today,
    "quantity": "1",
}

response = requests.post(url=graph_post_endpoint, json=graph_post_params, headers=headers)
print(response.text)


