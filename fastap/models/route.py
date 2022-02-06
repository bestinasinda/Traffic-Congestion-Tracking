import datetime

from sqlalchemy import Table, Column
from  sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta

routes = Table(
    'routes', meta,
    Column('id', Integer, primary_key=True),
    Column('route', String(255)),
    Column('status', String(255)),
    Column('update_at', String(244)),
)