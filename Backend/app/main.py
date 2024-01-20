from fastapi import FastAPI
from app.middleware.cors_middleware import get_cors_middleware

app = FastAPI()
app.add_middleware(get_cors_middleware)
