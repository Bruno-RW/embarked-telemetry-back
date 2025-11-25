from pydantic import BaseModel

from .location import Location
from .address import Address

class Telemetry(BaseModel):
    location: Location
    address: Address
