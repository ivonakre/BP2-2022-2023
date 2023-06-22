from . import Base
from sqlalchemy import *


class TipSobe (Base):
    __tablename__ = "tipSoba"
    ID_tipSobe = Column(Integer, primary_key = True)
    ime = Column(String(50))
    opis = Column(Text)
    cijena = Column(Integer)