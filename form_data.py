
from fastapi import FastAPI, Form
import uvicorn
app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')