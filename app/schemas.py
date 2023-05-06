from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class Token(BaseModel):
    access_token:str
    token_type:str

class UserPost(BaseModel):
    email:EmailStr
    password:str
    full_name:str
    address:str
    gender:str
    image:Optional[str]