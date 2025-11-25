from typing import List

from fastapi import APIRouter

from configs\
    import POSTGRE, QUERY_SELECT_LOCATION

from _types\
    import Location

LOCATION_ROUTER = APIRouter()

# ? === === === STATIC ROUTES === === === ?#
@LOCATION_ROUTER.get("/location", response_model=List[Location])
def getLocations():
    listLocations = POSTGRE.select(QUERY_SELECT_LOCATION)

    locationData = [
        Location(**location)
        for location 
        in listLocations
    ]

    return locationData