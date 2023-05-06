from fastapi import APIRouter, Depends , status, HTTPException,Response
from sqlalchemy.orm import Session
from ..databases import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas , models , utils , oauth2

router = APIRouter(
    tags = ['Authentication']
)

@router.post("/login",response_model = schemas.Token)
def login(user_credential:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username.lower()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Account does`nt exist")
    if user !=None:
        if not utils.verify(user_credential.password,user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Account does`nt exist")
    access_token = oauth2.create_access_token(data = {"id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}

@router.post('/register',status_code=status.HTTP_201_CREATED)
def register_user(userInfo:schemas.UserPost,db:Session = Depends(get_db)):
    userInfo.email = userInfo.email.lower()
    is_user = db.query(models.User).filter(models.User.email == userInfo.email).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"email with {userInfo.email} already taken!")
    userInfo.password = utils.hash(userInfo.password)
    user = models.User(**userInfo.dict())
    db.add(user)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED)
        