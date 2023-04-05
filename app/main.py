from fastapi.middleware.cors import CORSMiddleware
from . import databases, models
from fastapi import FastAPI


models.Base.metadata.create_all(bind=databases.engine)


app = FastAPI(
    debug=True
)

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_header=["*"]
)
