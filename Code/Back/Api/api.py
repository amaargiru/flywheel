import sys


from fastapi import FastAPI

sys.path.append('../Core')

from color_printer import ColorPrinter
from comparator import Comparator
from complicator import Complicator
from examiner import Examiner
from fw_logger import FlyWheelLogger
from lower import Lower
from refiner import Refiner

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello!": "Please read the docs: http://127.0.0.1:8000/docs"}


# http://127.0.0.1:8000/get_next_question?user_id=1
@app.get("/get_next_question")
def get_next_question(user_id: int):
    question_id = Examiner.define_next_question_num(user_id)
    question = Examiner.next_question(question_id)

    return {"question_id": question_id,
            "native_phrase": f"{question.native_phrase}"}
