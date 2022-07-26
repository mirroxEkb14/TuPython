
import sqlite3

# basic operations 'CRUD' - create/read/update/delete

try:
    conn = sqlite3.connect('accountant.db') # connect to the db
    cursor = conn.cursor() # get a cursor through which we make requests

    # create user with 'user_id' = 1000a
    cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (1000,))

    # get all the users
    users = cursor.execute("SELECT * FROM 'users'")
    print(users.fetchall())

    # commit the changes to save them in DB
    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if(conn):
        conn.close()


# SQL requests to create DB
"""
CREATE TABLE users (
    id        INTEGER  PRIMARY KEY AUTOINCREMENT,
    user_id   INTEGER  NOT NULL
                       UNIQUE,
    join_date DATETIME NOT NULL
                       DEFAULT ( (DATETIME('now') ) ) 
);

CREATE TABLE records (
    id        INTEGER  PRIMARY KEY AUTOINCREMENT,
    users_id  INTEGER  NOT NULL
                       REFERENCES users (id) ON DELETE CASCADE,
    operation BOOLEAN  NOT NULL,
    value     DECIMAL  NOT NULL,
    date      DATETIME NOT NULL
                       DEFAULT ( (DATETIME('now') ) ) 
);
"""
