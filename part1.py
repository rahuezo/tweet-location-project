from utils.configuration import (MAIN_DB_FILE, USERS_TBNAME, USERS_COLUMNS)
from utils.files import get_tweet_files, get_users_from_file
from utils.database import Database

import sqlite3, time


# Create main database

main_db = Database(MAIN_DB_FILE)

# Create users table 

users_tbname = main_db.create_table(USERS_TBNAME, USERS_COLUMNS)

# Get all tweet files 

all_tweet_files = get_tweet_files()

# Insert users into users table

start = time.time()

for tweet_file in all_tweet_files:    
    main_db.cursor.execute('BEGIN') 

    for user in get_users_from_file(tweet_file):
        main_db.insert('INSERT OR IGNORE INTO {tb_name} VALUES (?)'.format(tb_name=users_tbname), (user,))

    main_db.connection.commit()

print "Elapsed Time: {0}s".format(round(time.time() - start, 2))
