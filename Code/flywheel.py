from data_level import DataOperations as dop
from system_level import FileOperations as fop
from ui_level import UserOperations as uop

phrases_file_name: str = 'phrases.txt'
repetitions_file_name: str = 'repetitions.json'

if __name__ == '__main__':
    phrases_file_path = fop.find_or_create_file(phrases_file_name)
    repetitions_file_path = fop.find_or_create_file(repetitions_file_name)

    phrases: dict = fop.read_phrases(phrases_file_path)
    repetitions: dict = fop.read_repetitions(repetitions_file_path)
    can_work, assesment_error_message = dop.data_assessment(phrases, repetitions)

    if can_work:
        is_merged, merge_message = dop.merge(phrases, repetitions)
        print(merge_message)
        if is_merged:
            fop.save_repetitions(repetitions_file_path, repetitions)

        while True:
            current_phrase: str = dop.determine_next_phrase(repetitions)
            user_result: float = uop.user_session(current_phrase, repetitions)
            dop.update_repetitions(repetitions, current_phrase, user_result)
            fop.save_repetitions(repetitions_file_path, repetitions)
    else:
        print(assesment_error_message)
        exit()
