from .models import *


class DBManager:
    @staticmethod
    def start():
        db.create_tables([BotUser])
    
    @staticmethod
    def append_user(user_id):
        BotUser.create(user_id=user_id)
    
    @staticmethod
    def update_user(user_id, fi_name=None, finish_sub=None):
        data = {}
        if fi_name:
            data['fi_name'] = fi_name
        if finish_sub:
            data['finish_sub'] = finish_sub
        BotUser.update(**data).where(
            BotUser.user_id == user_id
        ).execute()

    @staticmethod
    def users() -> list[BotUser]:
        return BotUser.select()
    

    @staticmethod
    def delete_user(user_id):
        BotUser.delete().where(
            BotUser.user_id == user_id
        ).execute()


    @staticmethod
    def get_user(user_id) -> BotUser:
        return BotUser.get_or_none(BotUser.user_id == user_id)
        