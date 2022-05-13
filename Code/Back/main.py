import datetime
import pathlib
import sys
import time

from comparator import Comparator
from complicator import Complicator
from db_schema import User, Questionstat
from examiner import Examiner
from fw_logger import FlyWheelLogger
from lower import Lower
from printer import Printer
from refiner import Refiner

log_max_file_size = 1024 ** 2  # Максимальный размер одного файла логов
log_max_file_count = 10  # Максимальное количество файлов логов
log_file_path = "logs//fw.log"

if __name__ == '__main__':

    try:
        path = pathlib.Path(log_file_path)  # Создаем путь к файлу логов, если он не существует
        path.parent.mkdir(parents=True, exist_ok=True)
        logger = FlyWheelLogger.get_logger(log_file_path, log_max_file_size, log_max_file_count)
    except Exception as err:
        print(f"Error when trying to create log directory {str(err)}")
        sys.exit()  # Аварийный выход

    user_id: int = 1

    logger.info("Старт")

    question_id = Examiner.define_next_question_num(user_id)
    question = Examiner.get_question(question_id)
    user_input: str = input(f"Enter phrase \"{question.native_phrase}\" in english: ")
    user_input_cleaned = Refiner.refine_user_input(user_input)
    user_input_complex = Complicator.complicate_user_input(user_input_cleaned)
    user_input_without_punctuation_lower = Lower.list_lower(user_input_complex.user_input_without_punctuation)
    references_lower = Lower.references_lower(question.references)

    index, ratio = Comparator.find_nearest_reference_index(user_input_without_punctuation_lower, references_lower)
    correction = Comparator.find_matching_blocks(user_input_without_punctuation_lower, references_lower, index)
    Printer.color_print_message_to_user(question.references, index, correction, ratio)
    a = Printer.format_message_to_api(question.references, index, correction, ratio)

    current_user = User.get(User.username == "johndoe")
    # Refresh user data in DB
    current_user.attempts = int(current_user.attempts or 0) + 1
    time.strftime('%Y-%m-%d %H:%M:%S')
    current_user.last_visit = datetime.datetime.now()
    current_user.save(only=[User.attempts, User.last_visit])

    question_stat: Questionstat
    result = None

    try:
        result = Questionstat.get(Questionstat.username == current_user.username and Questionstat.question_id == question_id)
    except Exception as err:
        logger.error(f"Error when trying to load question_stat: {str(err)}")

    if result is not None:
        question_stat = result
        question_stat.question_stat = int(question_stat.question_stat or 0) + 1
        question_stat.last_attempt = datetime.datetime.now()
    else:
        question_stat = Questionstat.create(last_attempt=datetime.datetime.now(),
                                            question_id=question_id,
                                            question_stat=1,
                                            username=current_user.username)

    question_stat.save()
