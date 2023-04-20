from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'signups'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    def _str_(self):
        return self.name
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///project.sqlite',echo=True)
    Base.metadata.create_all(engine)