from datetime import datetime
from pydantic import BaseModel

class Location(BaseModel):
    id: str

    latitude: float | None
    longitude: float | None
    altitude: float | None

    hdop: float | None
    satellites: int | None
    
    date_time: datetime | None