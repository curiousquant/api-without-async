
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker, Session
from config import settings



# class Base(DeclarativeBase):
#     pass
# Base = declarative_base()

# engine = create_engine(url=settings.DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# def getdb():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()



class Base(DeclarativeBase):
    pass

engine = create_engine(url=settings.DATABASE_URL, echo=True)

def get_session():
    session = Session(bind=engine, expire_on_commit=False) 
    return session

def init_db():
    print(__name__)
    Base.metadata.create_all

