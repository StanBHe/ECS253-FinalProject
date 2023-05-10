import pandas
import numpy

kaggle_dataset_df = pandas.read_csv("steam-200k.csv")

all_steam_game_id_to_name = pandas.read_csv("steam_name_appid.csv")

kaggle_names_set = set(kaggle_dataset_df['name'])

#print(len(kaggle_names_set))

rslt_df = all_steam_game_id_to_name[all_steam_game_id_to_name['name'].isin(kaggle_names_set)]

rslt_df.to_csv('applicable_games_appid.csv', index=False, encoding='utf-8')