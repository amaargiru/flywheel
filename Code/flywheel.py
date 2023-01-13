phrases_file_name = "phrases.txt"
repetitions_file_name = "repetitions.json"

if __name__ == "__main__":
    phrases_file_path = find_or_create_file(phrases_file_name)
    repetitions_file_path = find_or_create_file(repetitions_file_name)

    phrases = read_phrases(phrases_file_path)
    repetitions = read_repetitions(repetitions_file_path)
    can_work, error_message = data_assessment(phrases, repetitions)

    if can_work:
        message = merge(repetitions, phrases)
        print(message)
        while True:
            current_phrase = determine_current_phrase(repetitions)
            user_result = user_session(current_phrase)
            update_repetitions(repetitions, current_phrase, user_result)
            save_repetitions(repetitions_file_path, repetitions)
    else:
        print(error_message)
        exit()
