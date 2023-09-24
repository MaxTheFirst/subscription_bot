from .check_user import is_privacy
from config import MIN_LENGHT_OF_NAME, MAX_LENGHT_OF_NAME, DATA_FORMAT
from dispatcher import bot, dp, timer
from bot_filters import admin_ids
from states import UserStates
from db import DBManager
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from datetime import date, timedelta 
from calendar import monthrange
import texts
import keyboards

@dp.message_handler(commands=[texts.START_COMMAND], commands_prefix=texts.PREFIX, state=None, is_admin=False)
async def on_start(message: Message):
    if not DBManager.get_user(message.from_user.id):
        await message.answer(texts.HELLOW)
        await UserStates.paste_name.set()
        DBManager.append_user(message.from_user.id)

def get_next_month():
    today = date.today()
    days = monthrange(today.year, today.month)[1]
    return today + timedelta(days=days)

async def send_to_admins(text: str, user_id, *args):
    text = text.format(*args)
    is_privacy_user = await is_privacy(user_id)
    keyboard = keyboards.get_admin_keyboard(user_id, is_privacy_user)
    for admin in admin_ids:
        await bot.send_message(admin, text, reply_markup=keyboard)

@dp.message_handler(state=UserStates.paste_name)
async def read_name(message: Message):
    name = message.text
    leng_name = len(name)
    if ' ' not in name or leng_name <= MIN_LENGHT_OF_NAME or leng_name >= MAX_LENGHT_OF_NAME:
        await message.answer(texts.ERROR_NAME)
        return
    user_id = message.from_user.id
    next_date = get_next_month()
    await message.answer(texts.THANKS.format(name, next_date.strftime(DATA_FORMAT)))
    DBManager.update_user(user_id, name, next_date)
    await dp.storage.set_state(user=message.from_user.id)
    await send_to_admins(texts.REG_TEXT, user_id, name, next_date.strftime(DATA_FORMAT))

@timer.time_handler()
async def send_push(user_id, name, text, is_finish):
    await bot.send_message(user_id, text, reply_markup=keyboards.pay)
    await dp.storage.set_state(user=user_id, state=UserStates.pay)
    if is_finish:
        await send_to_admins(texts.ADMIN_PAY_NO, user_id, name)

@dp.message_handler(Text(texts.PAY_KEY_TEXT), state=UserStates.pay)
async def click_pay(message: Message):
    await message.answer(texts.PAY_OK, reply_markup=ReplyKeyboardRemove())
    user_id = message.from_user.id
    await dp.storage.set_state(user=user_id)
    DBManager.update_user(user_id, finish_sub=get_next_month())
    user = DBManager.get_user(user_id)
    await send_to_admins(texts.ADMIN_PAY_OK, user_id, user.fi_name, user.finish_sub.strftime(DATA_FORMAT))