
from datetime import datetime, time, timedelta, date
from uuid import UUID
import uvicorn

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/")
async def read_items(

    start_date: date | None = Body(default=None),
    end_date: date | None = Body(default=None),

):
    duration = end_date - start_date
    return {

        "start_date": start_date,
        "end_date": end_date,
        "duration": duration,
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
