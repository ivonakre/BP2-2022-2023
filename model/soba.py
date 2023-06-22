from . import Base
from sqlalchemy import *


class Soba (Base):
    __tablename__ = "sobe"
    ID_soba = Column(Integer, primary_key = True)
    ime = Column(String(50))
    opis = Column(Text)
    status = Column(Text)

    tipSobe_id = Column(Integer, ForeignKey('tipSoba.ID_soba'))