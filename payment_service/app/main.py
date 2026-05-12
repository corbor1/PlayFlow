from fastapi import FastAPI
from payment_service.app.api.api import router as api_router
from contextlib import contextmanager

@contextmanager
def lifespan ():
    yield

app = FastAPI(lifespan = lifespan)

# Подключение роутера
app.include_router(api_router)

from config.config_models import DBConfig

config = DBConfig()
print(config)
host = config.host
print(host)