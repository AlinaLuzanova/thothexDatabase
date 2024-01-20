from fastapi.middleware.cors import CORSMiddleware


def get_cors_middleware(app):
    return CORSMiddleware(
        app,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
