from peewee import *

database = MySQLDatabase('flywheel', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                        'use_unicode': True, 'user': 'root', 'passwd': '8008'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Answer(BaseModel):
    english_phrase = CharField(column_name='englishPhrase')
    question_id = IntegerField(column_name='questionId')

    class Meta:
        table_name = 'answer'


class Question(BaseModel):
    native_phrase = CharField(column_name='nativePhrase')

    class Meta:
        table_name = 'question'


class Questionstat(BaseModel):
    question_id = IntegerField(column_name='questionId')
    question_stat = IntegerField(column_name='questionStat')
    user_id = IntegerField(column_name='userId', index=True)

    class Meta:
        table_name = 'questionstat'


class Questiontotheme(BaseModel):
    question_id = IntegerField(column_name='questionId')
    theme_id = IntegerField(column_name='themeId', index=True)

    class Meta:
        table_name = 'questiontotheme'


class Questiontoword(BaseModel):
    question_id = IntegerField(column_name='questionId')
    word_id = IntegerField(column_name='wordId', index=True)

    class Meta:
        table_name = 'questiontoword'


class Theme(BaseModel):
    theme = CharField()

    class Meta:
        table_name = 'theme'


class Themestat(BaseModel):
    theme_id = IntegerField(column_name='themeId')
    theme_stat = IntegerField(column_name='themeStat')
    user_id = IntegerField(column_name='userId', index=True)

    class Meta:
        table_name = 'themestat'


class User(BaseModel):
    attempts = IntegerField()
    email = CharField()
    last_visit = DateTimeField(column_name='lastVisit')
    level = IntegerField()
    name = CharField()
    password_hash = CharField(column_name='passwordHash')

    class Meta:
        table_name = 'user'


class Word(BaseModel):
    word = CharField()

    class Meta:
        table_name = 'word'


class Wordstat(BaseModel):
    user_id = IntegerField(column_name='userId', index=True)
    word_id = IntegerField(column_name='wordId')
    word_stat = IntegerField(column_name='wordStat')

    class Meta:
        table_name = 'wordstat'
