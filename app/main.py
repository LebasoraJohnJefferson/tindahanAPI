from fastapi.middleware.cors import CORSMiddleware
from . import databases, models
from fastapi import FastAPI
from .routes import auth

models.Base.metadata.create_all(bind=databases.engine)


app = FastAPI(
    debug=True
)

origins=['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def connected():
    return 'connected'

app.include_router(auth.router)
