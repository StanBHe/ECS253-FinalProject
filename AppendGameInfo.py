import pandas
import requests

#df = pandas.read_csv("applicable_games_appid.csv")
df = pandas.read_csv("applicable_games_appid_v4.csv")
# url = "http://steamspy.com/api.php?request=appdetails&appid={}".format(730)
# print(url)
# response = requests.get(url)
#print(response.json())

data = []
columns = ['appid', 'name', 'positive','negative','price', 'languages', 'genre', 'tags']

dataframe_size = len(df)
for index, row in df.iterrows():
    #print(row['appid'], row['name'])
    url = "http://steamspy.com/api.php?request=appdetails&appid={}".format(row['appid'])
    response = requests.get(url)
    response_params = [response.json().get('appid'), response.json().get('name'), response.json().get('positive'), response.json().get('negative'),
                response.json().get('price'),response.json().get('languages'),response.json().get('genre'),response.json().get('tags')]
    #print(response_params)
    data.append(response_params)
    print(index/dataframe_size * 100)

#print(df['tags'][0])
df = pandas.DataFrame(data = data, columns = columns)
df.to_csv('extracted_games_attributes_v4.csv', index=False, encoding='utf-8')