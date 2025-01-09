from pydantic import BaseModel
from datetime import datetime, date
class Flight(BaseModel):
    flight_number: str
    from_city : str
    to_city : str
    plane_id: int
    data_time: datetime

class Plane(BaseModel):
    model: str
    space_bus: int
    space_eco: int

class Ticket(BaseModel) :
    pasanger_id: int
    flight_id: int
    price: float
    class_type: int

class Passenger(BaseModel):
    fullname: str
    passport_id: str 
    phone_number: int
    birth_date: datetime  
    email: str

class Order(BaseModel):
    ticket_id:int 
    amount:int

class User(BaseModel):
    login:str
    password:str