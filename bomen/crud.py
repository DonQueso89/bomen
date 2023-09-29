from sqlalchemy.orm import Session

from bomen import models, schemas


def get_boom(db: Session, id_: int):
    return db.query(models.Boom).filter(models.Boom.id == id_).first()


def get_bomen(db: Session, limit: int = 10):
    return db.query(models.Boom).limit(limit).all()


def create_boom(db: Session, boom: schemas.BoomCreate) -> models.Boom:
    boom = models.Boom(**boom.model_dump())
    db.add(boom)
    db.commit()
    db.refresh(boom)
    return boom
