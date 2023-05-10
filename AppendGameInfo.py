import pandas
import requests

df = pandas.read_csv("applicable_games_appid.csv")


url = "http://steamspy.com/api.php?request=appdetails&appid={}".format(df.iloc[1].get("appid"))
print(url)
response = requests.get(url)

print(response.json())

# for index, row in df.iterrows():
#     print(row['appid'], row['name'])
    
#     url = "steamspy.com/api.php?request=appdetails&appid={}".format(row['appid'])
#     response = requests.get(url)