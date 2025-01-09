from pydantic import BaseModel
from datetime import datetime, date
class FlightModel(BaseModel):
    flight_number: str
    from_city : str
    to_city : str
    plane_id: int
    data_time: datetime

class PlaneModel(BaseModel):
    model: str
    space_bus: int
    space_eco: int

class TicketModel(BaseModel) :
    pasanger_id: int
    flight_id: int
    price: float
    class_type: int

class PassengerModel(BaseModel):
    fullname: str
    passport_id: str 
    phone_number: int
    birth_date: datetime  
    email: str

class OrderModel(BaseModel):
    ticket_id:int 
    amount:int

class UserModel(BaseModel):
    login:str
    password:str