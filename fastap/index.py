# run fastapi-    uvicorn index:app --reload
# get all routes /best-route
# get spec /best-route/{route_name}

from fastapi import  FastAPI
from routes.index import  route

app = FastAPI()

app.include_router(route)

