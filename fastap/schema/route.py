from pydantic import BaseModel


class Route(BaseModel):
    route: str
    status: str
    update_at: str