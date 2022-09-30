

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
