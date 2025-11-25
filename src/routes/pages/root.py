from fastapi.routing import APIRouter

ROOT_ROUTER = APIRouter()

@ROOT_ROUTER.get("/")
def root():
    return { "message": "Welcome to the FastAPI backend!" }
