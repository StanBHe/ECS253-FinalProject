import pandas as pd
import numpy
import json

with open('data.json', encoding='utf-8') as file:
    user_data = json.loads(file.read())

data = set()

for user in user_data.get("userData"):
    games_dict = user.get("games")
    data.update(games_dict.keys())

print(len(data))

with open('wishlist.json', encoding='utf-8') as file:
    wishlist_data = json.loads(file.read())
    
for user in wishlist_data.get("userData"):
    wish_game_list = user.get("wishlist")
    data.update(wish_game_list)
    print(wish_game_list)
    
print(len(data))

data.remove("success")

df = pd.DataFrame(data = data, columns = ['appid'])
df.to_csv('applicable_games_appid_v4.csv', index=False, encoding='utf-8')