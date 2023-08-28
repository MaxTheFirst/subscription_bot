from config import ADMINS
from aiogram import filters, types


admin_ids = []

class IsAdmin(filters.BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message) -> bool:
        if (message.from_user.username in ADMINS):
            if message.from_user.id not in admin_ids:
                admin_ids.append(message.from_user.id)
            return self.is_admin == True
        return self.is_admin == False

class CallbackCmd(filters.BoundFilter):
    key = 'callback_cmd'

    def __init__(self, callback_cmd):
        self.callback_cmd = callback_cmd

    async def check(self, callback: types.CallbackQuery):
        if callback.data:
            args = callback.data.split('_')
            if args[0] == self.callback_cmd[:-1]:
                if len(args) > 1:
                    return {'args': args[1::]}
                else:
                    return True
        return False

