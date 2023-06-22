from model import *
from model.relacije import *
from model.cache import region, api

#redis

rezervacije = session.query(Rezervacija).all()

for rezervacija in rezervacije:
    print(rezervacija.ID_rezervacija, rezervacija.datumDolaska + " " + rezervacija.datumOdlaska)

ID = 2
KEY = f'rezervacija_{ID}'
x = region.get(KEY)
print(x)
if x is api.NO_VALUE:
    x = session.query(Rezervacija).filter(Rezervacija.ID_rezervacija==ID).one()
    region.set(KEY, x)
print(x.datumDolaska + " " + x.datumOdlaska)