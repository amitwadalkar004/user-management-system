from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:Amit123%23@localhost:5433/postgres"

engine = create_engine(DATABASE_URL,echo=True)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=Sessionlocal()
    try :
        yield db
    finally:
        db.close()