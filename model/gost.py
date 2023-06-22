#. trenutni direktorij
#* označava sve
from . import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class Gost (Base):
    __tablename__ = "gosti"
    ID_gost = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    spol = Column(String(50))
    godiste = Column(Integer)
    adresa = Column(String(50))