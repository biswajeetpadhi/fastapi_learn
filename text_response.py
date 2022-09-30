

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
