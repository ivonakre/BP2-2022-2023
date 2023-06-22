from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#ovdje umjesto mysql treba localhost
#engine = create_engine("mysql://root:lozinka@localost:6306/hotel")
engine = create_engine("mysql+pymysql://hotel:lozinka@mysql:6306/hotel", connect_args={'unix_socket': None})

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()