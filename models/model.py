from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy_utils import EmailType
from dotenv import load_dotenv
load_dotenv()
import os 
user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASS_DB')
name_db = os.getenv('NAME_DB')

DATABASE_URL = 'postgresql://{user_db}:{pass_db}#5432@localhost/{name_db}'
engine = create_engine()
session = sessionmaker(autoslush=False,autocommit=False,bind=engine)
Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True)
    to_city = Column(str)
    plane_id = relationship("Plane",back_populates="flights")
    date_time = Column(DateTime)
class Plane(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    spaces_bus = Column(Integer)
    spaces_eco = Column(Integer)
    flights = relationship("Flight", back_populates="plane_id")
class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(str)
    passport_id = Column(str,index=True)
    birth_date = Column(DateTime)
    email = Column(EmailType)
    tickets = relationship("Ticket", back_populates="passenger_id")