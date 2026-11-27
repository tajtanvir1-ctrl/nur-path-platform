from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Nur Path', version='0.1.0')


class LiveStatus(BaseModel):
    status: Literal['alive'] = 'alive'


class NotReadyStatus(BaseModel):
    status: Literal['not_ready'] = 'not_ready'


@app.get('/api/v1/health/live', response_model=LiveStatus)
def live() -> LiveStatus:
    return LiveStatus()


@app.get('/api/v1/health/ready', status_code=503, response_model=NotReadyStatus)
def ready() -> NotReadyStatus:
    # Fail closed until actual database and dependency probes exist.
    return NotReadyStatus()
