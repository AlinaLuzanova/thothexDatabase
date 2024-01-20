from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def to_main():
    return {"message": "Hello World"}
