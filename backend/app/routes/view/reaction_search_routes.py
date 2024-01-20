from fastapi import APIRouter

router = APIRouter()


@router.get("/reaction_search")
def search_reactions():
    return {"reaction"}
