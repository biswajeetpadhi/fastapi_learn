
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
