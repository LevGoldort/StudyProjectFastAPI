import sqlite3

# define sqlite connection url
DATABASE_URL = "./rpg_api.db"

# create new engine instance
engine = sqlite3.connect(DATABASE_URL, check_same_thread=False)

# create session maker
if __name__ == "__main__":
    database_url = '.' + DATABASE_URL  # Create DB on main.py level
    base = sqlite3.connect(database_url)

    base.cursor().execute('''CREATE TABLE characters 
                            (char_id INTEGER PRIMARY KEY,
                             name varchar(20) NOT NULL,
                             dnd_class varchar(20) NOT NULL,
                             level varchar(20) NOT NULL,
                             race varchar(20) NOT NULL,
                             alignment varchar(20) NOT NULL)''')

    base.close()
