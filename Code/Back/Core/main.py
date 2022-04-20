import pathlib
import sys

import mysql.connector

from color_printer import ColorPrinter
from comparator import Comparator
from complicator import Complicator
from examiner import Examiner
from fw_logger import FlyWheelLogger
from lower import Lower
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

    mydb = mysql.connector.connect(host="localhost",
                                   user="amaargiru",
                                   password="8008",
                                   database="flywheel")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT nativePhrase, qReferences FROM question where id = 1")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    logger.info("Старт")
    question = Examiner.next_question()
    user_input: str = input(f"Enter phrase \"{question.native_phrase}\" in english: ")
    user_input_cleaned = Refiner.refine_user_input(user_input)
    user_input_complex = Complicator.complicate_user_input(user_input_cleaned)
    user_input_without_punctuation_lower = Lower.list_lower(user_input_complex.user_input_without_punctuation)
    references_lower = Lower.references_lower(question.references)

    index, ratio = Comparator.find_nearest_reference_index(user_input_without_punctuation_lower, references_lower)
    correction = Comparator.find_matching_blocks(user_input_without_punctuation_lower, references_lower, index)
    ColorPrinter.print_message_to_user(question.references, index, correction, ratio)
