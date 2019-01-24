import requests

def my_handler(event, context):
    url = "http://worldclockapi.com/api/json/est/now"

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "01d807d4-e0ba-4599-9daf-63e4c222174a"
        }

    response = requests.request("GET", url, headers=headers)

    return response
