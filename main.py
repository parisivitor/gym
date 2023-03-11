from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_302_FOUND
from fastapi import HTTPException, Response, Request
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from views import login
from sqlalchemy.exc import DBAPIError
from asyncpg.exceptions import StringDataRightTruncationError

api = FastAPI(title='GYM Goodzera')

api.include_router(login.router, tags=['Login'])


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
