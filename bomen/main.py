from typing import Annotated, Union

from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from bomen import crud, models, schemas
from bomen.db import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

MaxQuerySize = Annotated[str | None, Query(max_length=20)]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# public
@app.get("/bomen/{boom_id}", response_model=schemas.Boom)
async def get(boom_id: int, q: Union[str, None] = None, db: Session = Depends(get_db)):
    return crud.get_boom(db, boom_id)


# public
@app.get("/bomen/", response_model=list[schemas.Boom])
async def list(
    q: MaxQuerySize = None,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_bomen(db, limit)


# admins
@app.post("/bomen/", response_model=schemas.Boom)
async def create(boom: schemas.BoomCreate, db: Session = Depends(get_db)):
    return crud.create_boom(db, boom)


# admins
@app.put("/bomen/{boom_id}")
async def update(boom_id: int, boom: schemas.BoomUpdate | None, db: Session = Depends(get_db)):
    db_boom = crud.get_boom(db, boom_id)
    for fld in boom.model_fields:
        if (new_value := getattr(boom, fld)) is not None:
            setattr(db_boom, fld, new_value)
    
    db.commit()
    return db_boom
