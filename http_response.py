

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/typer")
async def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
