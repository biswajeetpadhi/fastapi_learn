

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()



if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
