from os import getpid

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Проект FastAPI для демонстрации балансировки нагрузки Nginx",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.get("/api/getpid", response_class=JSONResponse)
def fast():
    """
    Возвращает PID текущего экземпляра FastAPI
    """
    return JSONResponse(content={"pid": getpid()})


@app.get("/api/", response_class=JSONResponse)
def index():
    """
    Возвращает приветствие
    """
    return JSONResponse(content={"message": "FastAPI работает"})
