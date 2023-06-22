from . import Base
from sqlalchemy import *


class Racun (Base):
    __tablename__ = "racuni"
    ID_racun = Column(Integer, primary_key = True)
    datum = Column(DateTime)

    gost_id = Column(Integer, ForeignKey('gosti.ID_gost'))
    rezervacija_id = Column(Integer, ForeignKey('rezervacije.ID_rezervacija'))