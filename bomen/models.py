from sqlalchemy import Column, Integer, String

from bomen.db import Base


class Boom(Base):
    __tablename__ = "bomen"

    id = Column(Integer, primary_key=True, index=True)
    dutch_name = Column(String)
    scientific_name = Column(String)
    height = Column(String)
    type = Column(String)
    plant_year = Column(Integer)
    owner = Column(String)
    maintainer = Column(String)
    category = Column(String)
    genus = Column(String)
    sdview = Column(String)
    radius = Column(Integer)

    def __repr__(self) -> str:
        return F"<Boom dutch_name={self.id!r} height={self.height!r}"
