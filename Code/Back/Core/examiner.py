import re
from dataclasses import dataclass


@dataclass
class Question:
    native_phrase: str
    references: list[str]


class Examiner:
    @staticmethod
    def next_question(mycursor, question_id: int = 1) -> Question:
        mycursor.execute(f"SELECT nativePhrase, qReferences FROM question where id = {question_id}")
        myresult = mycursor.fetchall()

        native_phrase, q_references = myresult[0]
        a = re.findall('"([^"]*)"', native_phrase)[0]
        b = re.findall('"([^"]*)"', q_references)

        return Question(native_phrase=a, references=b)
