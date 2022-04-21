from dataclasses import dataclass

from db_schema import *


@dataclass
class UserQuestion:
    native_phrase: str
    references: list[str]


class Examiner:
    @staticmethod
    def next_question(question_id: int = 1) -> UserQuestion:
        native_phrase = Question.get(Question.id == question_id).native_phrase

        query = Answer.select().where(Answer.question_id == 1)

        references = []
        for pet in query:
            references.append(pet.english_phrase)

        return UserQuestion(native_phrase, references)
