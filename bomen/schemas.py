from enum import Enum

from pydantic import BaseModel


class Treetype(str, Enum):
    knotboom = "Knotboom"
    boom_vrij_uitgroeiend = "Boom vrij uitgroeiend"
    boom_niet_vrij_uitgroeiend = "Boom niet vrij uitgroeiend"
    fruitboom = "Fruitboom"
    leiboom = "Leiboom"
    gekandelaberde_boom = "Gekandelaberde boom"
    vormboom = "Vormboom"


class BoomBase(BaseModel):
    height: str | None = None  # Boomhoogte
    type: Treetype | None = None  # Boomtype
    plant_year: int | None = None  # Plantjaar
    owner: str | None = None  # Eigenaar
    maintainer: str | None = None  # Beheerder
    category: str | None = None  # Categorie
    genus: str | None = None  # SOORT_KORT
    sdview: str | None = None  # SDVIEW
    radius: int | None = None  # RADIUS


class BoomCreate(BoomBase):
    dutch_name: str  # Soortnaam_NL
    scientific_name: str  # Soortnaam_WTS

class BoomUpdate(BoomBase):
    dutch_name: str | None = None
    scientific_name: str | None = None 

class Boom(BoomBase):
    id: int

    class Config:
        orm_mode = True
