from typing import List

from fastapi import APIRouter

from configs\
    import POSTGRE, QUERY_SELECT_LOCATION, QUERY_SELECT_ADDRESS

from _types\
    import Location, Address, Telemetry

TELEMETRY_ROUTER = APIRouter()

# ? === === === STATIC ROUTES === === === ?#
@TELEMETRY_ROUTER.get("/telemetry", response_model=List[Telemetry])
def getTelemetry():
    listLocations = POSTGRE.select(QUERY_SELECT_LOCATION)
    listAddresses = POSTGRE.select(QUERY_SELECT_ADDRESS)

    telemetryData = [
        Telemetry(
            location=Location(**location),
            address=Address(**address)
        )
        for location, address 
        in zip(listLocations, listAddresses)
    ]

    return telemetryData