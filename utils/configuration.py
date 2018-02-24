import os 

MAIN_DB_HOME = 'results'
MAIN_DB_NAME = 'tweet_location_project.db'


def setup_db_home(): 
    if not os.path.exists(MAIN_DB_HOME): 
        os.makedirs(MAIN_DB_HOME)
        return os.path.join(MAIN_DB_HOME, MAIN_DB_NAME)
    return os.path.join(MAIN_DB_HOME, MAIN_DB_NAME)

MAIN_DB_FILE = setup_db_home()

USERS_TBNAME = 'users'
USERS_COLUMNS = 'user_id INT PRIMARY KEY, UNIQUE(user_id)'

TWEETS_TBNAME = 'tweets'
TWEETS_COLUMNS = 'user_id INT, tweet_text TEXT, tweet_location TEXT, tweet_date TEXT, county_fips INT'

    
    

