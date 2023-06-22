from . import Base
from sqlalchemy import *


class Osoblje (Base):
    __tablename__ = "cijene"
    ID_osoblje = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    opisPosla = Column(Text)
    spol = Column(String(50))