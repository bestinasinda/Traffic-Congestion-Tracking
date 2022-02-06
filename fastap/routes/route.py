# run fastapi- uvicorn index:app --reload

from fastapi import APIRouter
from config.db import conn
from models.index import routes
from schema.index import Route


route = APIRouter()


@route.get('/best-route/')
async def home():
    return conn.execute(routes.select()).fetchall()


@route.get('/best-route/{route_name}')
async def get_route(route_name: str):
    return conn.execute(routes.select().where(routes.c.route==route_name)).fetchall()
