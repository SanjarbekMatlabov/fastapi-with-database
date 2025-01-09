from sqlalchemy import create_engine,Column,Integer,String,DateTime,ForeignKey,Float
from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy_utils import EmailType
from dotenv import load_dotenv
load_dotenv()
import os 
user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASS_DB')
name_db = os.getenv('NAME_DB')

DATABASE_URL = "sqlite:///./ticket.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True)
    to_city = Column(String)
    plane_id = relationship("planes",back_populates="id")
    date_time = Column(DateTime)
class Plane(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    spaces_bus = Column(Integer)
    spaces_eco = Column(Integer)
    flights = relationship("flights", back_populates="plane_id")
class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    passport_id = Column(String,index=True)
    birth_date = Column(DateTime)
    email = Column(EmailType)
    tickets = relationship("Ticket", back_populates="passenger_id")
class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey('passengers.id'))
    flight_id = Column(Integer, ForeignKey('flights.id'))
    price = Column(Float)
    class_type = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    amount = Column(Integer)

Base.metadata.create_all(bind=engine)