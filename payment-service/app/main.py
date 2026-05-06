from fastapi import FastAPI
from api import router

app = FastAPI()

# Подключение роутера
app.include_router(router.router)


@app.get("/")
def root():
    return {"message": "Приложение работает!"}