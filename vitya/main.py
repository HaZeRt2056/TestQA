# from cgitb import reset
# from http.client import responses
#
# import requests
# from json.decoder import JSONDecodeError
# # #параметр
# # payload = {"name": "User"}
# #
# # response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# # print(response.text)
#
#
# # response = requests.get("https://playground.learnqa.ru/api/get_test")
# # print(response.text)
# #
# #
# # try:
# #     parsed_response_test = response.json()
# #     print(parsed_response_test)
# # except:
# #     print("Response is not a JSON format")
#
#
# import requests
#
# response = requests.get("https://playground.learnqa.ru/api/check_type")
# print(response.text)
#
# ### Request type: GET
#
# ###GET params:
#
# response = requests.post("https://playground.learnqa.ru/api/check_type")
# print(response.text)
#
# ### Request type: POST
#
# response = requests.delete("https://playground.learnqa.ru/api/check_type")
# print(response.text)
#
# ### Request type: D