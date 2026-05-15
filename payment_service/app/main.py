from fastapi import FastAPI
from app.api.api import router as api_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan (app:FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan = lifespan)

# Подключение роутера
app.include_router(api_router)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)

# from config.config_models import DBConfig

# config = DBConfig()
# print(config)
# host = config.host
# print(host)