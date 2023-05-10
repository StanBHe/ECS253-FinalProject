import pandas
import requests

df = pandas.read_csv("steam-200k.csv")
# print(df)
# print(type(df['user_id'][0]))

url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
response = requests.get(url)
#print(response.json())

extracted_json = response.json().get("applist").get("apps").get("app")

df_response = pandas.json_normalize(extracted_json)

#print(df_response)

df_response.to_csv('steam_name_appid.csv', index=False, encoding='utf-8')
