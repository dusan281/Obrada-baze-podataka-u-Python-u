import pandas as pd
import os

current_directory = os.getcwd()
print(f"Trenutni radni direktorijum je: {current_directory}")

# Učitajte CSV fajl
df = pd.read_csv('C:/Users/hp/Desktop/6 semestar/pmt/baza.csv')
df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'], format='%m/%d/%Y') 


df['Last_15_Results_Home'] = ''
df['Last_15_Results_Away'] = ''

def update_home_team_wins(df):
    df['HOME_TEAM_WINS'] = df['HOME_TEAM_WINS'].apply(lambda x: 'domaci_pobedio' if x == 1 else 'gost_pobedio')
    return df


def get_last_15_wins(team_id, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]


    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(15)

    wins_count = team_games.apply(lambda row: 1 if ((row['HOME_TEAM_ID'] == team_id and row['HOME_TEAM_WINS'] == 1) 
                                                    or (row['VISITOR_TEAM_ID'] == team_id and row['HOME_TEAM_WINS'] == 0)) else 0, axis=1).sum()
    
    return wins_count

# Funkcija za prosečan broj poena u poslednjih 15 utakmica
def average_points_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_points = team_games.apply(lambda row: row['PTS_home'] if row['HOME_TEAM_ID'] == team_id else row['PTS_away'], axis=1).sum()
    avg_points = total_points / len(team_games) if len(team_games) > 0 else 0
    return avg_points



def average_assists_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_assist = team_games.apply(lambda row: row['AST_home'] if row['HOME_TEAM_ID'] == team_id else row['AST_away'], axis=1).sum()
    avg_assist = total_assist / len(team_games) if len(team_games) > 0 else 0
    return avg_assist



def average_rebounds_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_rebounds = team_games.apply(lambda row: row['REB_home'] if row['HOME_TEAM_ID'] == team_id else row['REB_away'], axis=1).sum()
    avg_rebounds = total_rebounds / len(team_games) if len(team_games) > 0 else 0
    return avg_rebounds







def average_fg_pct_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_rebounds = team_games.apply(lambda row: row['FG_PCT_home'] if row['HOME_TEAM_ID'] == team_id else row['FG_PCT_away'], axis=1).sum()
    avg_rebounds = total_rebounds / len(team_games) if len(team_games) > 0 else 0
    return avg_rebounds








def average_ft_pct_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_rebounds = team_games.apply(lambda row: row['FT_PCT_home'] if row['HOME_TEAM_ID'] == team_id else row['FT_PCT_away'], axis=1).sum()
    avg_rebounds = total_rebounds / len(team_games) if len(team_games) > 0 else 0
    return avg_rebounds









def average_fg3_pct_last_n_games(team_id, n, date):
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    total_rebounds = team_games.apply(lambda row: row['FG3_PCT_home'] if row['HOME_TEAM_ID'] == team_id else row['FG3_PCT_away'], axis=1).sum()
    avg_rebounds = total_rebounds / len(team_games) if len(team_games) > 0 else 0
    return avg_rebounds







def average_opponent_points_last_n_games(team_id, n, date):
    average_opponent_points = 0
    team_games = df[((df['HOME_TEAM_ID'] == team_id) | (df['VISITOR_TEAM_ID'] == team_id)) & (df['GAME_DATE_EST'] < date)]
    team_games = team_games.sort_values(by='GAME_DATE_EST', ascending=False).head(n)
    for index, row in team_games.iterrows():
        if (row['HOME_TEAM_ID'] == team_id):
            average_opponent_points = average_opponent_points + row['PTS_away']
        else:
            average_opponent_points = average_opponent_points + row['PTS_home']
    return (average_opponent_points / n)




for index, row in df.iterrows():
    date = row['GAME_DATE_EST']
    home_team_id = row['HOME_TEAM_ID']
    away_team_id = row['VISITOR_TEAM_ID']


    df.at[index, 'Last_15_Results_Home'] = get_last_15_wins(home_team_id, date)
    df.at[index, 'Last_15_Results_Away'] = get_last_15_wins(away_team_id, date)


    df.at[index, 'Avg_PTS_last_15_Home'] = average_points_last_n_games(home_team_id, 15, date)



    df.at[index, 'Avg_AST_last_15_Home'] = average_assists_last_n_games(home_team_id, 15, date)


    df.at[index, 'Avg_REB_last_15_Home'] = average_rebounds_last_n_games(home_team_id, 15, date)


    df.at[index, 'Avg_fg_last_15_Home'] = average_fg_pct_last_n_games(home_team_id, 15, date)


    df.at[index, 'Avg_ft_last_15_Home'] = average_ft_pct_last_n_games(home_team_id, 15, date)



    df.at[index, 'Avg_fg3_last_15_Home'] = average_fg3_pct_last_n_games(home_team_id, 15, date)

 

    df.at[index, 'Avg_PTS_last_15_Away'] = average_points_last_n_games(away_team_id, 15, date)



    df.at[index, 'Avg_AST_last_15_Away'] = average_assists_last_n_games(away_team_id, 15, date)



    df.at[index, 'Avg_REB_last_15_Away'] = average_rebounds_last_n_games(away_team_id, 15, date)


    df.at[index, 'Avg_fg_last_15_Away'] = average_fg_pct_last_n_games(away_team_id, 15, date)



    df.at[index, 'Avg_ft_last_15_Away'] = average_ft_pct_last_n_games(away_team_id, 15, date)


    df.at[index, 'Avg_fg3_last_15_Away'] = average_fg3_pct_last_n_games(away_team_id, 15, date) 


    df.at[index, 'Avg_PTS_conceided_last_15_Home'] = average_opponent_points_last_n_games(home_team_id, 15, date)

    df.at[index, 'Avg_PTS_conceided_last_15_Away'] = average_opponent_points_last_n_games(away_team_id, 15, date)
    print(index) 


update_home_team_wins(df)
            





df.to_csv('Desktop/6 semestar/pmt/nba_games_with_last_5_results.csv', index=False)
print(df)
putanja_do_fajla = 'nba_games_with_last_5_results.csv'
if os.path.exists(putanja_do_fajla):
    print(f"CSV fajl '{putanja_do_fajla}' postoji.")
else:
    print(f"CSV fajl '{putanja_do_fajla}' ne postoji ili nije pristupačan.")



