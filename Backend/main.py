from fastapi import FastAPI
from app.middleware.cors_middleware import get_cors_middleware
from app.routes.view.main_routes import router as main_router
from app.routes.view.molecule_search_routes import router as molecule_search_router
from app.routes.view.reaction_search_routes import router as reaction_search_router

app = FastAPI()
app.add_middleware(get_cors_middleware)


app.include_router(main_router)
app.include_router(molecule_search_router)
app.include_router(reaction_search_router)