from asyncpg.exceptions import StringDataRightTruncationError
from fastapi import FastAPI
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import DBAPIError
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from views import login, seeds

api = FastAPI(title='GYM Goodzera')

api.include_router(login.router, tags=['Login'])
api.include_router(seeds.router, tags=['Seed'])


@api.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == HTTP_302_FOUND:
        return RedirectResponse(exc.headers["Location"])
    return JSONResponse(content={"message": exc.detail}, status_code=exc.status_code)


@api.exception_handler(DBAPIError)
async def handle_dbapi_error(request: Request, exc: DBAPIError):
    if isinstance(exc.orig, StringDataRightTruncationError):
        raise HTTPException(detail="exc.detail", status_code="exc.status_code")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:api", host="0.0.0.0", port=8000, log_level='info', reload=True)
