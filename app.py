from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List  # Import List for response model typing

from db import database, models
from schemas.player_schemas import PlayerCreate, PlayerResponse, PlayerUpdate
from crud import crud  # Import directly

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/players/")
def create_new_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

@app.get("/players/", response_model=List[PlayerResponse])  # Fixed response model type
def read_players(db: Session = Depends(get_db)):
    return crud.get_players(db)  # Fixed incorrect `crud.crud.get_players()`

@app.get("/players/{player_id}", response_model=PlayerResponse)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id=player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.put("/players/{player_id}", response_model=PlayerResponse)
def update_existing_player(player_id: int, player: PlayerUpdate, db: Session = Depends(get_db)):
    db_player = crud.update_player(db, player_id=player_id, player=player)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.delete("/players/{player_id}")
def delete_existing_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.delete_player(db, player_id=player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"message": "Player deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
