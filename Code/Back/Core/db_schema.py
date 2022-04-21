from peewee import *

database = MySQLDatabase('flywheel', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                        'use_unicode': True, 'user': 'root', 'passwd': '8008'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Answer(BaseModel):
    english_phrase = CharField(column_name='englishPhrase', null=True)
    question_id = IntegerField(column_name='questionId', null=True)

    class Meta:
        table_name = 'answer'


class Question(BaseModel):
    native_phrase = CharField(column_name='nativePhrase', null=True)

    class Meta:
        table_name = 'question'


class Questionstat(BaseModel):
    question_id = IntegerField(column_name='questionId', null=True)
    question_stat = IntegerField(column_name='questionStat', null=True)
    stat_id = AutoField(column_name='statId')
    user_id = IntegerField(column_name='userId', null=True)

    class Meta:
        table_name = 'questionstat'


class Theme(BaseModel):
    theme = CharField(null=True)

    class Meta:
        table_name = 'theme'


class Themestat(BaseModel):
    stat_id = AutoField(column_name='statId')
    theme_id = IntegerField(column_name='themeId', null=True)
    theme_stat = IntegerField(column_name='themeStat', null=True)
    user_id = IntegerField(column_name='userId', null=True)

    class Meta:
        table_name = 'themestat'


class User(BaseModel):
    attempts = IntegerField(null=True)
    email = CharField(null=True)
    last_visit = DateTimeField(column_name='lastVisit', null=True)
    level = CharField(null=True)
    name = CharField(null=True)
    password_hash = CharField(column_name='passwordHash', null=True)

    class Meta:
        table_name = 'user'


class Word(BaseModel):
    word = CharField(null=True)

    class Meta:
        table_name = 'word'


class Wordstat(BaseModel):
    stat_id = AutoField(column_name='statId')
    user_id = IntegerField(column_name='userId', null=True)
    word_id = IntegerField(column_name='wordId', null=True)
    word_stat = IntegerField(column_name='wordStat', null=True)

    class Meta:
        table_name = 'wordstat'
