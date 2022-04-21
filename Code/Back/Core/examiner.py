import re
from dataclasses import dataclass


@dataclass
class Question:
    native_phrase: str
    references: list[str]


class Examiner:
    @staticmethod
    def next_question(mycursor, question_id: int = 1) -> Question:
        mycursor.execute(f"SELECT nativePhrase FROM question where id = {question_id}")
        myresult = mycursor.fetchall()
        native_phrase = myresult[0][0]

        mycursor.execute(f"SELECT englishPhrase FROM answer where questionId = {question_id}")
        myresult = mycursor.fetchall()
        references = [x[0] for x in myresult]

        return Question(native_phrase, references)
