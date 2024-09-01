import requests
import datetime as dt
from secret import USER_NAME, TOKEN

yesterday = dt.datetime(year=2024, month=8, day=31).strftime(format="%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
graph_put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{yesterday}"


headers = {
    "X-USER-TOKEN": TOKEN
}

graph_put_params = {
    "quantity": "5",
}

response = requests.put(url=graph_put_endpoint, json=graph_put_params, headers=headers)
print(response.text)

