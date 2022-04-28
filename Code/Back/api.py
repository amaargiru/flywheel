import json

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from comparator import Comparator
from complicator import Complicator
from examiner import Examiner
from lower import Lower
from printer import Printer
from refiner import Refiner

app = FastAPI()

origins = [
    "http://domainname.com",
    "https://domainname.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # = origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# http://127.0.0.1:8000/docs
@app.get("/")
def read_root():
    return {"Hello!": "Please read the docs: http://127.0.0.1:8000/docs"}


# Example: http://127.0.0.1:8000/get_next_question?user_id=1
@app.get("/get_next_question")
def get_next_question(user_id: int):
    question_id = Examiner.define_next_question_num(user_id)
    question = Examiner.get_question(question_id)

    return {"question_id": question_id,
            "native_phrase": f"{question.native_phrase}"}


# Example: http://127.0.0.1:8000/get_answer_check?user_id=1&question_id=1&user_input=qq
@app.get("/get_answer_check")
def get_answer_check(user_id: int, question_id: int, user_input: str):
    question = Examiner.get_question(question_id)
    user_input_cleaned = Refiner.refine_user_input(user_input)
    user_input_complex = Complicator.complicate_user_input(user_input_cleaned)
    user_input_without_punctuation_lower = Lower.list_lower(user_input_complex.user_input_without_punctuation)
    references_lower = Lower.references_lower(question.references)
    index, ratio = Comparator.find_nearest_reference_index(user_input_without_punctuation_lower, references_lower)
    correction = Comparator.find_matching_blocks(user_input_without_punctuation_lower, references_lower, index)
    a = Printer.format_message_to_api(question.references, index, correction, ratio)

    return {"question_id": 1, "answer": json.dumps(a)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)