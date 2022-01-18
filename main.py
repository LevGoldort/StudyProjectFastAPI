from fastapi import FastAPI
from fastapi import Depends
from app import crud
from app.db import engine_connect

# initialize FastApi instance
app = FastAPI()


def get_db():
    db = engine_connect()
    return db


# define endpoint
@app.get("/")
def home():
    return {"Everything is connected"}


# define endpoint
@app.post("/create_character")
def create_character(name: str, dnd_class: str, level: int, race: str, alignment: str, db=Depends(get_db)):
    character = crud.create_character(db=db,
                                      name=name,
                                      dnd_class=dnd_class,
                                      level=level,
                                      race=race,
                                      alignment=alignment)
    db.close()
    return character


# get/retrieve character
@app.get("/get_character/{char_id}/")  # id is a path parameter
def get_character(char_id: int, db=Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
    Returns a character object if one with the given id exists, else null
    """
    character = crud.get_character(db=db, char_id=char_id)
    db.close()
    if not character:
        return {"error": f"Character with id {char_id} does not exist"}

    return character


@app.get("/list_characters")
def list_characters(db=Depends(get_db)):
    """
    Fetch a list of all Characters object
    Returns a list of objects
    """
    characters_list = crud.list_characters(db=db)
    db.close()
    return characters_list


@app.put("/update_character/{id}/")  # id is a path parameter
def update_character(char_id: int, name: str, dnd_class: str, level: int, race: str, alignment: str,
                     db=Depends(get_db)):
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
        db.close()
        return updated_character
    else:
        db.close()
        return {"error": f"Character with id {char_id} does not exist"}


@app.delete("/delete_character/{char_id}/")  # id is a path parameter
def delete_character(char_id: int, db=Depends(get_db)):
    # get character object from database
    db_character = crud.delete_character(db, char_id)
    # check if character object exists
    if not db_character:
        db.close()
        return {"error": f"Character with id {char_id} does not exist"}

    return db_character
