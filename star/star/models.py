from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('mysql+mysqldb://root@localhost:3306/xxx?charset=utf8')
Base = declarative_base()


class Star(Base):
    __tablename__ = 'avstar'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    birthday = Column(Date())
    image_urls = Column(String(64))
    height = Column(Integer())
    cup = Column(String(64))
    bust = Column(Integer())
    waist = Column(Integer())
    hips = Column(Integer())

if __name__ == '__main__':
    Base.metadata.create_all(engine)
