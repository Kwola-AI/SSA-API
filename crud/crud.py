from sqlalchemy.orm import Session
from db.models import PlayerDetails
from schemas.player_schemas import PlayerCreate, PlayerUpdate

def create_player(db: Session, player: PlayerCreate):
    db_player = PlayerDetails(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players(db: Session):
    return db.query(PlayerDetails).all()

def get_player(db: Session, player_id: int):
    return db.query(PlayerDetails).filter(PlayerDetails.id == player_id).first()

def update_player(db: Session, player_id: int, player: PlayerUpdate):
    db_player = db.query(PlayerDetails).filter(PlayerDetails.id == player_id).first()
    if db_player:
        for key, value in player.dict(exclude_unset=True).items():
            setattr(db_player, key, value)
        db.commit()
        db.refresh(db_player)
    return db_player

def delete_player(db: Session, player_id: int):
    db_player = db.query(PlayerDetails).filter(PlayerDetails.id == player_id).first()
    if db_player:
        db.delete(db_player)
        db.commit()
    return db_player
