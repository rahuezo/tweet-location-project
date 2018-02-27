from utils.configuration import (MAIN_DB_FILE, USERS_TBNAME, USERS_COLUMNS, TWEETS_TBNAME, TWEETS_COLUMNS)
from utils.files import get_tweet_files, get_users_from_file, get_tweets_from_file
from utils.database import Database

import sqlite3, time, sys


# Create main database

main_db = Database(MAIN_DB_FILE)

# Create users table 

tweets_tbname = main_db.create_table(TWEETS_TBNAME, TWEETS_COLUMNS)

# Get all tweet files 

all_tweet_files = get_tweet_files()

# Insert users into users table

start = time.time()

for i, tweet_file in enumerate(all_tweet_files):
    if i % 100 == 0: 
        print '{} out of {} - {}'.format(i + 1, len(all_tweet_files), round(time.time() - start, 2))

    main_db.cursor.execute('BEGIN') 

    tweets = [t for t in get_tweets_from_file(tweet_file)]
    main_db.insert('INSERT INTO {tb_name} VALUES (?, ?, ?, ?, ?)'.format(tb_name=tweets_tbname), tweets, many=True)

    main_db.connection.commit()
 
print "Elapsed Time: {0}s".format(round(time.time() - start, 2))
