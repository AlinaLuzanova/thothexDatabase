from fastapi import APIRouter

router = APIRouter()


@router.get("/molecule_search")
def search_molecule():
    return {"molecule"}
