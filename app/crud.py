
"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Character


def db_add(db, character):
    cur = db.cursor()
    cur.execute("INSERT INTO characters(name, dnd_class, level, race, alignment)  VALUES (?,?,?,?,?)", (
        character.name,
        character.dnd_class,
        character.level,
        character.race,
        character.alignment
    ))
    db.commit()


def db_get(db, char_id):

    db_select = db.execute("SELECT * FROM characters WHERE char_id = ?", (str(char_id),))

    for row in db_select:
        return row  # executes if there is at least one row

    return None  # no rows found


def db_get_all(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM characters")
    db.commit()
    return cur.fetchall()


def db_update(db, char_id, new_character):
    old_character = db_get(db, char_id)

    if not old_character:
        return None

    cur = db.cursor()
    param_tuple = (
                new_character.name,
                new_character.dnd_class,
                new_character.level,
                new_character.race,
                new_character.alignment,
                char_id)
    cur.execute('''UPDATE characters SET 
                name = ? ,
                dnd_class = ? ,
                level = ? ,
                race = ? ,
                alignment = ?
                WHERE char_id = ?
                ''',
                param_tuple)
    db.commit()
    return new_character


def db_delete(db, char_id):
    cur = db.cursor()
    deleted_character = db_get(db, char_id)

    if not deleted_character:
        return None

    cur.execute('''DELETE FROM characters where char_id = ?''', (char_id,))
    db.commit()

    return deleted_character


def create_character(db, name, dnd_class, level, race, alignment):
    """
    function to create a character model object and put it to db
    """
    # create character instance
    new_character = Character(name=name, dnd_class=dnd_class, level=level, race=race, alignment=alignment)

    db_add(db, new_character)

    return new_character


def get_character(db, char_id: int):
    """
    get the character record with a given id, if no such record exists, will return null
    """
    db_character = db_get(db, char_id)
    return db_character


def list_characters(db):
    """
    Return a list of all existing character records
    """
    all_characters = db_get_all(db)
    return all_characters


def update_character(db, char_id: int, name: str, dnd_class: str, level: int, race: str, alignment: str):
    """
    Update a Character object's attributes
    """
    new_character = Character(name=name,
                              dnd_class=dnd_class,
                              level=level,
                              race=race,
                              alignment=alignment)

    res = db_update(db=db, char_id=char_id, new_character=new_character)

    return res


def delete_character(db, char_id: int):
    """
    Delete a Character object
    """
    deleted_character = db_delete(db, char_id)
    return deleted_character
