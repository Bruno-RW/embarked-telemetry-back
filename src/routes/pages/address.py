from typing import List

from fastapi import APIRouter

from configs\
    import POSTGRE, QUERY_SELECT_ADDRESS

from _types\
    import Address

ADDRESS_ROUTER = APIRouter()

# ? === === === STATIC ROUTES === === === ?#
@ADDRESS_ROUTER.get("/address", response_model=List[Address])
def getAddresses():
    listAddresses = POSTGRE.select(QUERY_SELECT_ADDRESS)

    addressData = [
        Address(**address)
        for address 
        in listAddresses
    ]

    return addressData