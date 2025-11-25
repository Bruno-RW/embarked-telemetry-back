from configs\
    import APP, PREFIX_V1

from .pages\
    import ROOT_ROUTER, LOCATION_ROUTER, ADDRESS_ROUTER, TELEMETRY_ROUTER

def setupRoutes():
    APP.include_router(ROOT_ROUTER, tags=["Root"])

    APP.include_router(LOCATION_ROUTER, prefix=PREFIX_V1, tags=["Location"])
    APP.include_router(ADDRESS_ROUTER, prefix=PREFIX_V1, tags=["Address"])
    
    APP.include_router(TELEMETRY_ROUTER, prefix=PREFIX_V1, tags=["Telemetry"])