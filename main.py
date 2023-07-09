import requests
from datetime import datetime
USERNAME = "benhombrebueno"
TOKEN = "$8CcqODNtz*4TV*Tm#Y2C"
GRAPH_ID = "pygraph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    "thanksCode":"ThisIsThanksCode"
}

#response = requests.post(url=pixela_endpoint, json=user_params)



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name": "Python Programming",
    "unit":"minutes",
    "type":"float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

add_pixel_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
date_today = datetime.now()
mod_date = date_today.strftime("%Y%m%d")

add_pixel_data_config = {
    "date":date_today.strftime("%Y%m%d"),
    "quantity":"60.0"
}

#response = requests.post(url=add_pixel_data_endpoint, json=add_pixel_data_config, headers=headers)
#print(response.text)


modify_pixel_data_endpoint = f"{add_pixel_data_endpoint}/20230528"
modify_pixel_data_config = {
    "quantity":"50.0"
}
# response = requests.put(url=modify_pixel_data_endpoint, json=modify_pixel_data_config,headers=headers)
# print(response.text)

delete_pixel_data_endpoint = f"{add_pixel_data_endpoint}/20230528"

response = requests.delete(url=delete_pixel_data_endpoint,headers=headers)
print(response.text)
