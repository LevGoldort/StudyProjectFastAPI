from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Character


def create_character(db: Session, name, dnd_class, level, race, alignment):
    """
    function to create a character model object
    """
    # create friend instance
    new_character = Character(name=name, dnd_class=dnd_class, level=level, race=race, alignment=alignment)
    # place object in the database session
    db.add(new_character)
    # commit your instance to the database
    db.commit()
    # refresh the attributes of the given instance
    db.refresh(new_character)
    return new_character


def get_character(db: Session, char_id: int):
    """
    get the character record with a given id, if no such record exists, will return null
    """
    db_character = db.query(Character).filter(Character.id == char_id).first()
    return db_character


def list_characters(db: Session):
    """
    Return a list of all existing character records
    """
    all_friends = db.query(Character).all()
    return all_friends


def update_character(db: Session, char_id: int, name: str, dnd_class: str, level: int, race: str, alignment: str):
    """
    Update a Character object's attributes
    """
    db_character = get_character(db=db, char_id=char_id)
    db_character.name = name
    db_character.dnd_class = dnd_class
    db_character.level = level
    db_character.race = race
    db_character.alignment = alignment

    db.commit()
    db.refresh(db_character)  # refresh the attribute of the given instance
    return db_character


def delete_character(db: Session, char_id: int):
    """
    Delete a Character object
    """
    db_character = get_character(db=db, char_id=char_id)
    db.delete(db_character)
    db.commit()  # save changes to db
