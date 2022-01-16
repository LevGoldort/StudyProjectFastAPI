import sqlite3

# define sqlite connection url
SQLALCHEMY_DATABASE_URL = "../rpg_sqlite.db"

# create new engine instance
engine = sqlite3.connect(SQLALCHEMY_DATABASE_URL)

# create session maker
SessionLocal = engine.cursor()
if __name__ == "__main__":
    try:
        SessionLocal.execute('''CREATE TABLE characters
                       (char_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name, 
                       dnd_class, 
                       level, 
                       race, 
                       alignment)''')
        engine.commit()

    except:
        print('table "Characters" already exists')

    engine.close()
