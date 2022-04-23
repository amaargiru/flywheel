from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_next_question")
def get_next_question(item_id: Optional[int] = 1, q: Optional[str] = None):
    return {"question_id": 1,
            "native_phrase": "Кот",
            "q": q}
