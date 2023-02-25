## Duolingo на минималках

Привет, меня зовут Емельянов Михаил, я Python-программист и я хотел бы показать вам свой небольшой «проект выходного дня» — **Flywheel**, микро-платформу для изучения иностранных языков — смесь Duolingo и Anki, программу, которая может помочь вам правильно **писать** на английском. Flywheel доступен в исходниках, лежит на [GitHub](https://github.com/amaargiru/flywheel).

![Flywheel](https://raw.githubusercontent.com/amaargiru/flywheel/main/pics/Dorothy.png)

Как вы, возможно, знаете, обобщенное знание иностранного языка можно разложить на четыре относительно независимые составляющие: чтение, письмо, слушание и говорение. К сожалению, тренировка одной из этих способностей не будет напрямую отражаться на остальных компонентах, поэтому, например, развивая навык чтения, мы достаточно опосредованно влияем на навык письма. Flywheel — «точилка» именно для **письменного английского**.

Если вы когда-нибудь пользовались Duolingo, то имеете представление о формате, в котором будет идти обучение. Последовательность проста: вот тебе фраза, переведи её на другой язык; программа запомнит, когда ты в последний раз переводил ту или иную фразу и насколько успешно у тебя это получилось; в зависимости от правильности ответа будет определено время, когда тебе нужно задать эту же фразу еще раз. В целом, на мой взгляд, как сам Duolingo, так и используемый им подход — просто гениальны. Но... Есть нюансы, которые несколько портят впечатления от процесса учёбы, и именно для их устранения я и задумал Flywheel.

### Хотелки

Во-первых, и это самое главное, я хотел бы, чтобы все задания на перевод были *только* русско-английскими. Я хочу видеть только русские фразы, которые мне нужно перевести на английский. Переводить с английского на русский не хочу. Я не учусь на переводчика, я хочу изучить иностранный язык! А для этого гораздо правильнее, на мой взгляд, вообще не включать русскоязычную раскладку на клавиатуре во время учёбы. На Duolingo есть небольшой «лайфхак» — переключение с изучения английского для русскоговорящих на изучение *русского для англоговорящих* (этим, отчасти, и объясняется большое количество учащихся на этом курсе — в основном это вовсе не американцы или жители туманного Альбиона, изучающие русский, а как раз наоборот, жители России, зубрящие английский язык), тогда учебный курс будет содержать больше русско-английских заданий, но количество англо-русских переводов всё равно останется очень большим. А я хочу 100 % времени урока писать на английском!

Во-вторых, я взрослый человек, и мне совершенно не нужна геймификация процесса обучения. Всё эти человечки, весело подмигивающие, приободряющие и дающие советы — один сплошной жирный, неуместный и раздражающий Круциатус. Доходит даже до выпуска расширений для браузера, которые пытаются вырезать весь этот ненужный функционал, сведя визуал сайта до необходимого уровня минимализма.

Третье — я взрослый человек (повторяюсь, да) и у меня иногда нет времени на полноразмерный урок. Хотя на Duolingo он довольно короток, но, тем не менее, разбивка процесса обучения на фиксированный уроки по ...надцать вопросов удобна в первую очередь для обучающей платформы, а не для ученика. Я хочу, чтобы у меня была возможность повтора не двадцати фраз, а, скажем, пяти или трёх, даже одной, наконец. Хочу прерывать процесс обучения в любой момент без потери прогресса! В конце концов, я иногда могу заниматься только в редкие перерывы недетерминированной продолжительности между моими основными активностями, под чай с печенькой, или в передышке между общением с детьми. Если у меня есть буквально свободная минута, то я хочу сделать пару подходов и сохранить свой прогресс.

В-четвертых, хочу иметь возможность всегда, на любом этапе обучения добавлять новые фразы! Услышав или вычитав что-то новое, полезное или просто интересное, хочу добавить фразу в список, пусть теперь программа позаботится о том, чтобы я эта фраза осталась в моей памяти навсегда.

Пятое, и тоже немаловажное соображение — хочу, чтобы программа показывала неправильно введенные фрагменты перевода. Иногда в введенном тексте есть мелкие ошибки, опечатки, «поймать» которые глазами довольно затруднительно. Надо, чтобы программа наглядно показывала разницу между моим переводом и правильным вариантом, а я бы сосредоточился на изучении английского, а не на игре «найди ошибочную букву в длинной фразе на иностранном языке».

Вот такой вот список пожеланий у меня накопился — хочу Duolingo, но только с русско-английскими заданиями, без геймификации, с сохранением прогресса после каждого задания, с возможностью добавлять новые фразы и с визуализацией сделанных ошибок, даже мелких.

Думаю, на этом предисловие можно закончить и перейти к сути. Если вы просто хотите начать учить английский язык — переходите к следующему разделу, «Использование». Если вы хотите посмотреть, как программа устроена «под капотом», то переходите разделу «Как это работает» (ближе к концу статьи).

### Использование

Использование Flywheel предельно просто. В самом начале у вас есть всего один файл — phrases.txt (в файле, идущем вместе с программой, около двух тысяч фраз). Там вы можете видеть множество фразовых пар, просто разделенных двойной вертикальной чертой, например:

*Я люблю тебя || I love you*

Если русскую фразу можно корректно перевести несколькими разными английскими фразами, то для их разделения используется одиночная вертикальная черта:

*Я живу в этом городе || I live in this city | I live in this town*

Наконец, если существуют две русскоязычные фразы, которые тоже могут иметь множество эквивалентных переводов, то для их разделения также используется одиночная вертикальная черта:

*Кот сидит на столе | Кошка сидит на столе || A cat sits on the table | The cat sits on the table*

Последнюю фразовую пару можно еще немного усложнить:

*Кот сидит на столе | Кошка сидит на столе || A cat sits on the table | The cat sits on the table | A cat is sitting on the table | The cat is sitting on the table*

Разумеется, в phrases.txt можно и нужно добавлять **собственные фразовые пары**. В этом-то и состоит самый цимес Flywheel — не обязательно зубрить то, что содержится в словаре, это просто заготовка. Корректируйте содержание уроков под свой уровень владения языком; перемещайте наиболее полезные, на ваш взгляд, фразовые пары повыше в словаре; добавляйте пары, связанные с вашей профессиональной деятельностью. Не говоря уже о том, что оболочке всё равно, какой язык вы учите. Хотите изучать испанский — bienvenido! Хотите изучать алеутский — да не вопрос. Хотите изучать алеутский, будучи носителем испанского? Легко!

Пожалуйста, не добавляйте в словарь слова! Разумеется, технически это возможно, но с точки зрения эффективности изучения языка не очень оправдано. Постарайтесь добавлять именно фразы, а если хотите добавить в свою личную копилку какое-нибудь конкретное новое слово, лучше возьмите фразу, где оно применяется в конкретном контексте. Так вы не только лучше запомните это слово, но и легче переведете его из пассивной фазы в активную — будете не просто распознавать его в тексте или в устной речи, но и начнете применять его при письме и при говорении.

Теперь просто запустите flywheel.py. В папке с программой появятся еще два файла — repetitions.json (здесь будет записан ваш прогресс и степень запоминания всех пройденных фразовых пар) и user_statistics.txt (здесь будет записано общее количество сделанных вами упражнений и будет сформирован общий список слов, которые вы успели изучить).

### Как это работает

Если вы — начинающий Python-разработчик и хотите поточить зубки обо что-нибудь простенькое, но не бесполезное, попробуйте Flywheel. Возможно, вам удастся прикрутить к нему какую-нибудь убервостребованную фичу, а в процессе отладки еще и английский подтяните. Разумеется, большую часть методов, используемых в программе, описывать особого смысла не имеет, остановлюсь только на общем подходе и на ключевых функциях, имеющих непосредственное отношение к анализу прогресса пользователя.

В последнее время я стал практиковать следующий метод: пишу заготовку main, *как будто бы* все методы программы уже разработаны и мне просто осталось их вызвать. Это позволяет взглянуть на код с высоты, так сказать, птичьего полёта (даже если высота полёта вызывает ассоциации скорее с пингвином, а не с орлом :) и оценить примерный уровень планируемых трудозатрат. В этот раз получилось следующее:

```python
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
```

Логика работы примерно такова:  
• найдём в каталогах проекта файл phrases.txt (множество фразовых пар, разделенных двойной вертикальной чертой, подробности читайте в разделе «Использование»); если найти его не удалось, создадим пустышку для будущего редактирования пользователем;  
• аналогично, поищем файл repetitions.json (записи прогресса и степень запоминания всех пройденных фразовых пар), если не нашли — создаем пустой файл;  
• создаем структуры данных из информации, считанной из phrases.txt и repetitions.json, а потом оцениваем, можно ли работать с такой комбинацией. Не пустой phrases.txt — OK, мы сможем преобразовать фразовые пары в наш внутренний формат и переписать эту информацию в repetitions.json. Не пустой repetitions.json — тоже OK, можем работать с уже накопленной информацией. А вот две пустышки, и phrases.txt, и repetitions.json — уже не OK, нам просто неоткуда черпать информацию, необходимую для работы — жалуемся на этот факт пользователю, пусть создаст phrases.txt хоть с каким-то минимальным содержимым;  
• в цикле подбрасываем пользователю новое задание, выбирая из фразового словаря ту фразу, которая наиболее актуальна на настоящий момент. Если есть фразы, требующие повторения, в первую очередь берем именно их; если все пройденные задания не требуют освежения памяти прямо сейчас, то начинаем подкидывать новые фразы.  
• после каждого задания, вне зависимости от качества ответа, обновляем информацию в repetitions.json и статистику пользователя.

В процессе написания кода я разбил весь функционал на data_level (это, своего рода, квинтэссенция собственно языковой практики), system_level (функционал, зависящий от операционной системы) и ui_level (методы, определяющие способ взаимодействия с пользователем) плюс добавил файл статистики, отображающий общее количество «подходов», предпринятых пользователем, а также содержащий все как английские, так и русские слова, пройденные им в процессе обучения. Окончательный вариант получился примерно тем же самым, что и первоначальная заготовка, только чуточку разлапистее:

```python
from data_level import DataOperations as dop
from system_level import FileOperations as fop
from ui_level import UiOperations as uop

phrases_file_name: str = 'phrases.txt'
repetitions_file_name: str = 'repetitions.json'
statistics_file_name: str = 'user_statistics.txt'

if __name__ == '__main__':
    phrases_file_path = fop.find_or_create_file(phrases_file_name)
    repetitions_file_path = fop.find_or_create_file(repetitions_file_name)
    user_statistics_file_path = fop.find_or_create_file(statistics_file_name)

    phrases: dict = fop.read_phrases(phrases_file_path)
    repetitions: dict = fop.read_json_from_file(repetitions_file_path)
    can_work, assesment_error_message = dop.data_assessment(phrases, repetitions)

    statistics: dict = fop.read_json_from_file(user_statistics_file_path)

    if can_work:
        is_merged, merge_message = dop.merge(phrases, repetitions)
        print(merge_message)
        if is_merged:
            fop.save_json_to_file(repetitions_file_path, repetitions)

        while True:
            current_phrase: str = dop.determine_next_phrase(repetitions)
            user_result, best_translation = uop.user_session(current_phrase, repetitions[current_phrase])

            dop.update_repetitions(repetitions, current_phrase, user_result)
            fop.save_json_to_file(repetitions_file_path, repetitions)

            statistics = dop.update_statistics(statistics, current_phrase, best_translation)
            fop.save_json_to_file(statistics_file_name, statistics)
    else:
        print(assesment_error_message)
        exit()
```

Сначала нужно определить, правильно ли ответил пользователь на предложенный вопрос, с учётом возможного существования нескольких правильных вариантов перевода:

```python
# import jellyfish

def find_max_string_similarity(user_input: str, translations: str | List[str]) -> (float, str):
    """Compares user_input against each string in translations"""
    max_distance: float = 0

    if isinstance(translations, str):
        translations = [translations]
    best_translation: str = translations[0]

    # Cleanup and 'compactify' user input ('I   don't know!!!😀' -> 'i dont know')
    user_input = DataOperations._compact(DataOperations._cleanup_user_input(user_input).lower())

    # 'Compactify' translations
    translations = [(t, DataOperations._compact(t.lower())) for t in translations]

    for translation, compact_translation in translations:
        current_distance = jellyfish.jaro_distance(user_input, compact_translation)

        if current_distance > max_distance:
            max_distance = current_distance
            best_translation = translation

    return max_distance, best_translation

def _compact(input_string: str) -> str:
    """Restrict use of all special characters and allow letters and numbers only"""
    return ''.join(ch for ch in input_string if ch.isalnum() or ch == ' ')
```

Внутри шелухи, занятой переливанием данных, вы можете видеть вычисление расстояния Джаро:

```python
current_distance = jellyfish.jaro_distance()
```

И, соответственно, есть оценка правильности ответа пользователя:

```python
level_excellent: float = 0.99
level_good: float = 0.97
level_mediocre: float = 0.65
```

Прикиньте, может быть, тут более уместно будет расстояние Левенштейна?

Попробуйте, кстати, превратить вот это:

```Python
user_input = DataOperations._compact(DataOperations._cleanup_user_input(user_input).lower())
```

примерно вот в это (я имею в виду не выкидывание DataOperations, а организацию пайпа методов типа string):

```Python
user_input = user_input.lower().cleanup().compact()
```

К сожалению, добавление собственных методов к встроенным типам в Python требует или применения субклассов, или использования велосипедов типа forbiddenfruit (уже немножко умер) / fishhook (еще немножко сыроват). А ведь в C# эта возможность встроена из коробки, аргхх...

Алгоритм интервальных повторений, в зависимости от качества ответа решающий, когда именно пройденная фраза будет предложена пользователю в следующий раз, построен на базе [SuperMemo-2](https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm):

```python
def _supermemo2(repetition: dict, user_result: float) -> dict:
    """Update next attempt time based on user result"""
    if user_result >= DataOperations.level_good:  # Correct response
        if repetition['repetition_number'] == 0:  # + 1 day
            repetition['time_to_repeat'] = (datetime.now() + timedelta(days=1)).strftime(datetime_format)
        elif repetition['repetition_number'] == 1:  # + 6 days
            repetition['time_to_repeat'] = (datetime.now() + timedelta(days=6)).strftime(datetime_format)
        else:  # + (6 * easiness_factor) days
            repetition['time_to_repeat'] = (datetime.now()
                                            + timedelta(days=6 * repetition['easiness_factor'])).strftime(datetime_format)
        repetition['repetition_number'] += 1
    else:  # Incorrect response
        repetition['repetition_number'] = 0

    repetition['easiness_factor'] = repetition['easiness_factor'] + (
            0.1 - (5 - 5 * user_result) * (0.08 + (5 - 5 * user_result) * 0.02))
    repetition['easiness_factor'] = max(repetition['easiness_factor'], 1.3)

    return repetition
```

В семействе алгоритмов SuperMemo есть более свежие реализации, вплоть до SuperMemo-18. Вы можете перейти на их использование, специально для этого в repetitions.json предусмотрено хранение нескольких последних попыток пользователя:

```python
max_attempts_len: int = 10  # Limit for 'Attempts' list
```

Заодно попробуйте разобраться, почему, при наличии SuperMemo-18, по сию пору активно используется SuperMemo-2, а самые рисковые разработчики не уходят дальше SuperMemo-5 или, максимум, упрощенного SuperMemo-8. Почитайте заодно про [A Trainable Spaced Repetition Model for Language Learning](https://github.com/duolingo/halflife-regression/blob/master/settles.acl16.pdf), алгоритм, опубликованный разработчиками Duolingo, в которой они пытались устранить недочеты предыдущих подходов. Попробуйте повторить ключевой функционал Duolingo, это вполне реализуемая возможность.

Далее идёт сохранение полученных результатов, думаю, останавливаться подробно на реализации этого функционала необходимости нет.

Теперь, когда ответ пользователя уже взвешен и учтён, нужно показать ученику не просто правильный вариант, а подробности, помогающие локализовать ошибки. Для этого вначале сформируем структуру данных, содержащую информацию о разности между желаемым и фактическим результатом:

```python
# from dataclasses import dataclass
# from difflib import SequenceMatcher

def find_user_mistakes(user_input: str, reference: str) -> list:
    """Dig for user errors and typos"""

    @dataclass
    class ComplexPhrase:
        phrase_without_punctuation: List[str]
        transformation_matrix: List[int]

    user_input = DataOperations._cleanup_user_input(user_input).lower()
    reference = reference.lower()
    correction_map: list[bool] = [True] * len(reference)

    complex_reference: ComplexPhrase = ComplexPhrase(phrase_without_punctuation=[], transformation_matrix=[])

    # 'Minify' reference phrase and remember transformation shifts
    for i, ch in enumerate(reference):
        if ch.isalnum() or ch == ' ':
            complex_reference.phrase_without_punctuation.append(ch)
            complex_reference.transformation_matrix.append(i)

    minified_reference: str = ''.join(complex_reference.phrase_without_punctuation)
    corr_map: list[bool] = [False] * len(minified_reference)

    # Compare cleaned user input and 'minified' reference
    seq = SequenceMatcher(lambda ch: not (ch.isalnum() or ch == ' '), user_input, minified_reference)
    blocks = seq.get_matching_blocks()
    blocks = blocks[:-1]  # Last element is a dummy

    for _, i, n in blocks:
        if n >= 3:  # Don't show to the user too short groups of correct letters, perhaps he entered a completely different phrase
            for x in range(i, i + n):
                corr_map[x] = True

    # 'Unminify' reference phrase and restore transformation shifts
    for i, corr in enumerate(corr_map):
        if corr is False:
            correction_map[complex_reference.transformation_matrix[i]] = False

    return correction_map
```

Немножко сложновато? На первый взгляд, можно было пойти более коротким путём, напрямую применив SequenceMatcher к пользовательскому ответу и референсной фразе, примерно вот так:

```python
def find_user_mistakes(user_input: str, reference: str) -> list:
    """Display of user errors"""
    seq = SequenceMatcher(None,
                            "".join(DataOperations._compact(DataOperations._cleanup_user_input(user_input).lower())),
                            DataOperations._compact(reference.lower()))
    blocks = seq.get_matching_blocks()
    blocks = blocks[:-1]  # Last element is a dummy

    corr_map: list = [False] * len(reference)

    for _, i, n in blocks:
        if n >= 3:  # Don't show to the user too short groups of correct letters, perhaps he entered a completely different word
            for x in range(i, i + n):
                corr_map[x] = True

    return corr_map
```

Вместо этого мы «заворачиваем», а потом «разворачиваем» какую-то дополнительную структуру данных, которая хранит далеко не все символы исходного текста, но зато помнит, какие символы куда смещены. Зачем?

Дело в том, что одной из ключевых фич Duolingo является игнорирование знаков препинания и разницы между прописными и заглавными буквами. Например, вместо «Hello! My name is Kitty» вполне допустимо ввести «hello my name is kitty», и это очень круто. Мы же, в конце концов, в первую очередь изучаем грамматику иностранного языка, уже в целом владея правилами написания имен и расстановки знаков препинания (хотя в английском и здесь есть свои особенности), и получение незачёта за написание, скажем, имени Michael с прописной буквы было бы, конечно, мощной просадкой всего юзер экспириенса.

Такую же вкусняшку я захотел внедрить и в Flywheel. Именно поэтому референсная фраза и ответ пользователя сначала сворачиваются в «чистый текст», без знаков препинания и заглавных букв, потом сравниваются, а в конце референсная фраза снова разворачивается в полный ответ, показываемый пользователю.

Далее, чтобы наглядно показать пользователю ошибки и опечатки, сформируем полноцветный пользовательский вывод, фразу, в которой цвет символа будет зависеть от правильности его написания:

```python
def _print_colored_diff(correction, reference) -> None:
    """Visualisation of user errors"""
    for i, ch in enumerate(reference):
        if correction[i]:
            print(Fore.GREEN + ch, end='')
        else:
            if ch != ' ':
                print(Fore.RED + ch, end='')  # Just a letter
            else:
                if i - 1 >= 0 and i + 1 < len(reference):  # Emphasise the space between correct but sticky characters
                    if correction[i - 1] and correction[i + 1]:
                        print(Fore.RED + '_', end='')
                    else:
                        print(Fore.RED + ' ', end='')
```

На этом жизненный цикл очередного вопроса в консольном приложении заканчивается.

Хотите примерно то же самое, но по-взрослому (а то вроде как-то фу заставлять пользователя выходить из программы по Ctrl-C) — с веб-интерфейсом, базой данных, ORM, API и голосовыми подсказками? Покопайтесь в папке [flywheel/Legacy](https://github.com/amaargiru/flywheel/tree/main/Legacy). Там лежит рабочий код, отличающийся от последней микро-версии, описанной в этой статье, менее консистентным data_level (в частности, я, не зная о SuperMemo, пытался изобрести свой собственный алгоритм интервальных повторений), но зато там есть все упомянутые плюшки. Возможно, тихий хлопок одной ладонью, зовущий вас обратно в консоль, вы услышите чуть позже... А пока можете попробовать запилить собственный стартап, создав потенциального соперника Duolingo, Cerego, Course Hero или Memrise.

### Выведение

Ну что ж, пожалуй, на этом пока всё. С настоящего момента и до конца своего текущего жизненного цикла вы можете тратить на изучение иностранного языка именно столько времени, сколько удобно именно вам, добавлять новые фразы или дополнять существующие переводы и сохранять прогресс даже после микроскопического усилия.

Не забывайте, однако, о том, что:  
во-первых, чудес не бывает, и при любом раскладе вам придется потратить на изучение языка существенное время ([приблизительные оценки](https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours) от британских учёных);  
и, во-вторых, по меткому замечанию Ильи Франка, «Язык похож на ледяную горку – на нее надо быстро взбежать; пока не взбежите — будете скатываться», т. е., другими словами, если вы не выделите на изучение языка достаточно много времени, причем укладываясь в достаточно сжатые сроки, вам не удастся достигнуть новой точки равновесия, приобретенные знания медленно, но надежно уйдут.

Если у вас остались вопросы, жду вас в комментариях. Напоминаю, что программа Flywheel доступна в исходниках, лежит на [GitHub](https://github.com/amaargiru/flywheel), по возможности обновляется и исправляется. Если вас заинтересовал такой достаточно немудрёный, но, на мой взгляд, весьма эффективный метод изучения английского языка, пожалуйста, создавайте форки репозитария, корректируйте как код (проект написан на Python и содержит всего около четырехсот строк), так и список переведенных фраз. Если поставите на GitHub'е звёздочку — будет просто супер, может быть, пригодится когда-нибудь на собеседовании; всё-таки свитер с дырками от орденов завсегда выглядит солиднее, чем просто свитер, даже если это был памятный знак «40 лет пионерлагерю "Орлёнок"» :)

И знаете, что мне нравится в таком методе больше всего? За несколько дней использования программы мой английский, конечно, сильно не улучшился. Но! У меня появилось достаточно отчётливое чувство контроля над процессом изучения иностранного языка! Раньше, при использовании того же Duolingo, меня не покидало ощущение некоторой пассивности, чувство пассажира машинки, намертво приваренной к остову аттракциона: вот машинка начинает двигаться, вот резко дёргается вправо, вот плавный левый поворот... Траектория, возможно, была и неплоха, и научно обоснована, но вот беда — никак не учитывала мои предыдущие знания и индивидуальные предпочтения. Теперь же, когда у меня в руках находятся и данные, и методы их обработки, я чувствую, что мой автомобильчик худо-бедно начинает слушаться руля и едет-таки в нужном именно мне направлении.
