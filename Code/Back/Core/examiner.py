import secrets
from dataclasses import dataclass

from db_schema import *


@dataclass
class UserQuestion:
    native_phrase: str
    references: list[str]


class Examiner:
    @staticmethod
    def define_next_question_num(user_id: int = 1) -> int:
        question_db_table_len = database.execute_sql("SELECT COUNT(*) FROM question").fetchone()[0]
        question_num = secrets.randbelow(question_db_table_len) + 1
        return question_num

    @staticmethod
    def next_question(question_id: int = 1) -> UserQuestion:
        native_phrase = Question.get(Question.id == question_id).native_phrase
        query = Answer.select().where(Answer.question_id == question_id)

        references = []
        for ref in query:
            references.append(ref.english_phrase)

        return UserQuestion(native_phrase, references)
