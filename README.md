# FastAPI Route Logger

### Usage

```python
from typing import Union

from fastapi import FastAPI

from route_logger_middleware import GlobalLoggerMiddleware
from route_logger_middleware.backends.mqtt_backend import MQTTBackend

app = FastAPI()

backend = MQTTBackend(hostname="localhost", topic="logs")
app.add_middleware(GlobalLoggerMiddleware, backend=backend, module_name="my-awesome-app")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```