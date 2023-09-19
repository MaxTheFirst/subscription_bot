from db import DBManager
from texts import REQUEST_PAY
from datetime import datetime
from asyncio import sleep

class UserTimer():
    def __init__(self):
        self.func = None
    
    def time_handler(self):
        def wrapper(func):
            self.func = func
        return wrapper
    
    async def wait_normal(self):
        time = datetime.now()
        while time.minute != 0:
            await sleep(60)
            time = datetime.now()

    async def check(self):
        time_deltas = list(REQUEST_PAY)
        finish_delta = min(*time_deltas)
        while True:
            users = DBManager.users()
            for user in users:
                time_x = datetime(user.finish_sub.year, user.finish_sub.month, user.finish_sub.day)
                time = datetime.now()
                delta = round((time_x-time).total_seconds() / 3600)
                if delta in time_deltas:
                    is_finish = delta == finish_delta
                    await self.func(user.user_id, user.fi_name, REQUEST_PAY[delta], is_finish)
            await sleep(3600)
    
    async def run(self):
        await self.wait_normal()
        await self.check()