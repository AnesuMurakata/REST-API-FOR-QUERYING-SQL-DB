import falcon
import argparse
import sqlalchemy

from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from models import User, Post, Group 
from middleware import SQLAlchemySessionManager
from resources import UserResource

Base = declarative_base()
engine = create_engine('sqlite+pysqlite:///file.db', module=sqlite)
session_factory = sessionmaker(bind=engine)

api = falcon.API(middleware=[SQLAlchemySessionManager(session_factory)])
api.add_route('/user', UserResource())


