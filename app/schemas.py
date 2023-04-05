from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class Token(BaseModel):
    access_token:str
    token_type:str