from dispatcher import dp, timer
from handlers import *
import asyncio


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(timer.run())
    loop.create_task(dp.start_polling())
    loop.run_forever()


if __name__ == '__main__':
    main()
