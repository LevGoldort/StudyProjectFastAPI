from fastapi import FastAPI
from fastapi import Depends
from app import crud
from app.db import engine
from sqlalchemy.orm import Session

# initialize FastApi instance
app = FastAPI()


def get_db():
    db = engine
    return db


# define endpoint
@app.get("/")
def home():
    return {"Everything is connected"}


# define endpoint
@app.post("/create_character")
def create_character(name: str, dnd_class: str, level: int, race: str, alignment: str, db: Session = Depends(get_db)):
    character = crud.create_character(db=db,
                                      name=name,
                                      dnd_class=dnd_class,
                                      level=level,
                                      race=race,
                                      alignment=alignment)
    return character


# get/retrieve friend
@app.get("/get_character/{char_id}/")  # id is a path parameter
def get_character(char_id: int, db: Session = Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
    Returns a character object if one with the given id exists, else null
    """
    character = crud.get_character(db=db, char_id=char_id)
    return character


@app.get("/list_characters")
def list_friends(db: Session = Depends(get_db)):
    """
    Fetch a list of all Friend object
    Returns a list of objects
    """
    friends_list = crud.list_characters(db=db)
    return friends_list


@app.put("/update_character/{id}/")  # id is a path parameter
def update_character(char_id: int, name: str, dnd_class: str, level: int, race: str, alignment: str,
                     db: Session = Depends(get_db)):
    # get character object from database
    db_character = crud.get_character(db=db, char_id=char_id)
    # check if character object exists
    if db_character:
        updated_character = crud.update_character(db=db,
                                                  char_id=char_id,
                                                  name=name,
                                                  dnd_class=dnd_class,
                                                  level=level,
                                                  race=race,
                                                  alignment=alignment)
        return updated_character
    else:
        return {"error": f"Friend with id {char_id} does not exist"}


@app.delete("/delete_character/{char_id}/")  # id is a path parameter
def delete_friend(char_id: int, db: Session = Depends(get_db)):
    # get character object from database
    db_character = crud.get_character(db=db, char_id=char_id)
    # check if character object exists
    if db_character:
        return crud.delete_character(db=db, char_id=char_id)
    else:
        return {"error": f"Character with id {char_id} does not exist"}
