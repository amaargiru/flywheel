import secrets
from dataclasses import dataclass

from db_schema import database, Question, Answer


@dataclass
class UserQuestion:
    native_phrase: str
    references: list[str]
    links_to_audio: list[str]


class Examiner:
    @staticmethod
    def define_next_question_num(user_id: int = 1) -> int:
        question_db_table_len = database.execute_sql("SELECT COUNT(*) FROM question").fetchone()[0]
        question_num = secrets.randbelow(question_db_table_len) + 1
        return question_num

    @staticmethod
    def get_question(question_id: int = 1) -> UserQuestion:
        native_phrase = Question.get(Question.id == question_id).native_phrase
        query = Answer.select().where(Answer.question_id == question_id)

        references = []
        for ref in query:
            references.append(ref.english_phrase)

        links_to_audio = []
        for ref in query:
            links_to_audio.append(ref.link_to_audio)

        return UserQuestion(native_phrase, references, links_to_audio)
