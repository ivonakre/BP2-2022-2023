from sqlalchemy.orm import relationship

from .soba import Soba
from .tipSobe import TipSobe
from .rezervacija import Rezervacija
from .racun import Racun
from .osoblje import Osoblje
from .gost import Gost
from . import Base
from . import engine

Soba.tipSobe = relationship("TipSobe", back_populates="sobe")
Soba.rezervacije = relationship("Rezervacija", back_populates="soba")
TipSobe.sobe = relationship("Soba", back_populates="tipSobe")
Rezervacija.soba = relationship("Soba", back_populates="rezervacije")
Rezervacija.racuni = relationship("Racun", back_populates="rezervacija")
Rezervacija.osoblje = relationship("Osoblje", back_populates="rezervacije")
Rezervacija.gost = relationship("Gost", back_populates="rezervacije")
Racun.rezervacija = relationship("Rezervacija", back_populates="racuni")
Osoblje.rezervacije = relationship("Rezervacija", back_populates="osoblje")
Gost.rezervacije = relationship("Rezervacija", back_populates="gost")

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)