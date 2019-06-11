from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

#association_table models the many to many relationship between users and groups
association_table = Table('association', Base.metadata,
    Column('users_username', String, ForeignKey('users.username')),
    Column('groups_id', Integer, ForeignKey('groups.id'))
)

class User(Base):
     __tablename__ = 'users'

     #id = Column(Integer, primary_key=True)
     firstname = Column(String)
     lastname = Column(String)
     username = Column(String, primary_key=True)
     email = Column(String)
     password = Column(String)

     posts = relationship("Post", back_populates="user") 
     groups = relationship("Group", secondary=association_table, back_populates="users")

     def __repr__(self):
        return "<User(firstname='%s', lastname='%s', nickname='%s')>" % (
                             self.firstname, self.lastname, self.nickname)

class Post(Base):
     __tablename__ = 'posts'

     id = Column(Integer, primary_key=True)
     votes = Column(Integer)
     title = Column(String, nullable=False)
     body = Column(String, nullable=False)
     group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
     user_name = Column(String, ForeignKey('users.username'), nullable=False)

     user = relationship("User", back_populates="posts")

     def __repr__(self):
         return "<Post(title='%s')>" % self.title 

class Group(Base):
     __tablename__ = 'groups'

     id = Column(Integer, primary_key=True)
     group_name = Column(String, nullable=False)

     users = relationship("User", secondary=association_table, back_populates="groups")

     def __repr__(self):
         return "<Group(name='%s', id='%s')>" % (self.name, self.id)