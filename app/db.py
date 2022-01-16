import sqlite3

# define sqlite connection url
SQLALCHEMY_DATABASE_URL = "../rpg_sqlite.db"

# create new engine instance
engine = sqlite3.connect(SQLALCHEMY_DATABASE_URL, check_same_thread=False)

# create session maker
SessionLocal = engine.cursor()
if __name__ == "__main__":
    SessionLocal.execute('''CREATE TABLE characters 
                            (char_id INTEGER PRIMARY KEY,
                             name varchar(20) NOT NULL,
                             dnd_class varchar(20) NOT NULL,
                             level varchar(20) NOT NULL,
                             race varchar(20) NOT NULL,
                             alignment varchar(20) NOT NULL)''')
    SessionLocal.execute("INSERT INTO characters(name, dnd_class, level, race, alignment) VALUES (?,?,?,?,?)", (
        "character.name",
        "character.dnd_class",
        "character.level",
        "character.race",
        "character.alignment"))
    engine.commit()

    engine.close()
