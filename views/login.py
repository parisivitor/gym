from datetime import datetime

import psycopg2.errorcodes
from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import RedirectResponse

from core.auth import autenticar, criar_token_acesso
from core.deps import get_session, remove_auth
from core.security import gerar_hash_senha
from core.deps import get_session, get_current_user

from models.person_model import PersonModel
from schemas.person_schema import PersonSchemasBase, PersonSchemaCreate

router = APIRouter()

@router.get("/logout")
def login(request: Request):
    response = RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    remove_auth(response)

    return response



@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=PersonSchemasBase)
async def post_person(person: PersonSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_person: PersonModel = PersonModel(cpf=person.cpf, name=person.name, lastname=person.lastname, celphone=person.celphone,
                                               password=gerar_hash_senha(person.password), created_at=datetime.now(), updated_at=datetime.now())

    async with db as session:
        try:
            session.add(new_person)
            await session.commit()

            return new_person
        except IntegrityError as e:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e.orig.args[0].split("DETAIL")[1]))
        except DBAPIError as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e.orig.args[0].split(":")[1]))




@router.post('/login', status_code=status.HTTP_200_OK)
async def login_empregador(response: Response,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_session)):

    person = await autenticar(cpf=form_data.username, password=form_data.password, db=db)


    if not person:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User or Password is incorrect")

    access_token = criar_token_acesso(sub=person.uuid)
    response.set_cookie("access_token", access_token, secure=False, httponly=True)

    return JSONResponse(content={"access_token": criar_token_acesso(sub=person.uuid), "token_type": "bearer"})


@router.get('/logado', response_model=PersonSchemasBase)
def get_logado(person_logado: PersonModel = Depends(get_current_user)):
    return person_logado