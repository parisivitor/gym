from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.configs import settings
from core.security import verificar_senha
from models.person_model import PersonModel

oauthe2_schema = OAuth2PasswordBearer(tokenUrl="token")


async def autenticar(cpf: str, password: str, db: AsyncSession) -> Optional[PersonModel]:
    async with db as session:
        query = select(PersonModel).filter(PersonModel.cpf == cpf)
        result = await session.execute(query)
        person: PersonModel = result.scalars().unique().one_or_none()

        if not person:
            return None

        if not verificar_senha(password, person.password):
            return None

        return person


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # https://datatracker/ietf/org/doc/html/rfc7519#section-4.1.3
    payload = {}

    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_vida

    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io
    """
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )