from pydantic import BaseModel

class Address(BaseModel):
    id: str

    country: str | None
    country_code: str | None

    state: str | None
    region: str | None

    city: str | None
    postcode: str | None
    road: str | None
    house_number: int | None