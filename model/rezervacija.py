from . import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class Rezervacija (Base):
    __tablename__ = "rezervacije"
    ID_rezervacija = Column(Integer, primary_key =True)
    datumDolaska = Column(Date)
    datumOdlaska = Column(Date)
    ukupnaCijena = Column(Integer)

    soba_id = Column(Integer, ForeignKey('sobe.ID_soba'))
    osoblje_id = Column(Integer, ForeignKey('osoblja.ID_osoblje'))
    gost_id = Column(Integer, ForeignKey('gosti.ID_gost'))