from fastapi import FastAPI
from api import router as api_router

app = FastAPI()

# Подключение роутера
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Приложение работает!"}