from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/bot_db', echo=True)
# engine = create_engine('mysql+pymysql://nizom:nizom0299@localhost:3306/web_bot', echo=True)

Base = declarative_base()

meta = MetaData()

check = Table(
    'Laravel_web_bot', meta,
    Column('chat_id', String, primary_key=True),
    Column('type', String),
)
meta.create_all(engine)


class Customers(Base):
    __tablename__ = 'Laravel_web_bot'

    chat_id = Column(String, primary_key=True)
    type = Column(String)


async def new_user_add(chat_id, type):
    Session = sessionmaker(bind=engine)
    session = Session()
    customer = Customers(
        chat_id=chat_id,
        type=type,
    )
    session.add(customer)
    session.commit()


async def getUserList():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.type == "user")
    return result


async def getGroupList():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.type == "group").all()
    return result


async def getUsersCount():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.type == "user").count()
    return result


async def getGroupsCount():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.type == "group").count()
    return result
