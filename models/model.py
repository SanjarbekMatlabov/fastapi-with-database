from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = 'postgresql://{USER_DB}:{PASS_DB}#5432@localhost/{NAME_DB}'
engine = create_engine()
session = sessionmaker
Base = declarative_base()