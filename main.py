from fastapi import FastAPI
from app import models
from app.db import engine
from app.db import SessionLocal
from fastapi import Depends
from app import crud
from sqlalchemy.orm import Session


# initailize FastApi instance
app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# define endpoint
@app.get("/")
def home():
    return {"Ahoy": "Captain"}


#define endpoint
@app.post("/create_character")
def create_character(name: str, dnd_class: str, level: int, race: str, alignment: str, db: Session = Depends(get_db)):
    character = crud.create_character(db=db, name=name, dnd_class=dnd_class, level=level, race=race, alignment=alignment)
    return character

# get/retrieve friend
@app.get("/get_character/{id}/") #id is a path parameter
def get_character(id: int, db: Session = Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
    Returns a character object if one with the given id exists, else null
    """
    character = crud.get_character(db=db, id=id)
    return character


@app.get("/list_characters")
def list_friends(db:Session = Depends(get_db)):
    """
    Fetch a list of all Friend object
    Returns a list of objects
    """
    friends_list = crud.list_characters(db=db)
    return friends_list


@app.put("/update_character/{id}/") #id is a path parameter
def update_character(id:int, name: str, dnd_class: str, level: int, race: str, alignment: str,
                     db: Session = Depends(get_db)):
    #get friend object from database
    db_character = crud.get_character(db=db, id=id)
    #check if friend object exists
    if db_character:
        updated_character = crud.update_character(db=db, id=id, name=name, dnd_class=dnd_class, level=level, race=race,
                                               alignment=alignment)
        return updated_character
    else:
        return {"error": f"Friend with id {id} does not exist"}


@app.delete("/delete_friend/{id}/") #id is a path parameter
def delete_friend(id:int, db: Session=Depends(get_db)):
    #get friend object from database
    db_character = crud.get_character(db=db, id=id)
    #check if friend object exists
    if db_character:
        return crud.delete_character(db=db, id=id)
    else:
        return {"error": f"Friend with id {id} does not exist"}