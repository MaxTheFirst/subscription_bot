from peewee import *

db = SqliteDatabase('db/users.db')


class BaseModel(Model):
    class Meta:
        primary_key = False
        database = db


class BotUser(BaseModel):
    user_id = IntegerField()
    fi_name = CharField(null=True)
    finish_sub = DateField(null=True)

    class Meta:
        db_table = 'bot_users'