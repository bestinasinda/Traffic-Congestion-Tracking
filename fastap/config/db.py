from sqlalchemy import create_engine, MetaData
import pymysql
engine = create_engine("mysql+pymysql://root@localhost:3306/route")
meta = MetaData()

conn = engine.connect()
