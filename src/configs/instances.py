
from databases import PostgreUtil
POSTGRE = PostgreUtil()


from fastapi import FastAPI
APP = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)