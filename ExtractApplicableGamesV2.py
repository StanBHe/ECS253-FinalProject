import pandas
import numpy

all_steam_game_id_to_name = pandas.read_csv("steam_name_appid.csv")

all_steam_game_id_to_name.to_csv('applicable_games_appid_v2.csv', index=False, encoding='utf-8')