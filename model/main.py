from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
Engine = create_engine('sqlite:///db_sis.sqlite3')