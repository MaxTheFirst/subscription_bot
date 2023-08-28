from texts import *
from config import MAX_COUNT_BTN
from db import DBManager
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

pay = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(PAY_KEY_TEXT))

def get_user_button(text, key, user_id):
    return InlineKeyboardButton(text, callback_data=key+str(user_id))

def get_admin_keyboard(user_id, delete_btn=False):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(USER_KEY_TEXT, url=USER_URL.format(user_id))
    ).add(
        get_user_button(UPDATE_DATE, UPDATE_KEY, user_id)
    )
    if delete_btn:
        keyboard.add(
            get_user_button(DELETE, DELETE_CMD, user_id)
        )
    return keyboard

def get_users_keyboard(start_index=0):
    stop_index = start_index + MAX_COUNT_BTN
    users = DBManager.users()
    if not users:
        return None
    keyboard = InlineKeyboardMarkup()
    for user in users[start_index:stop_index]:
        keyboard.add(
            get_user_button(user.fi_name, CHOOSE_KEY, user.user_id)
        )
    btns = []
    if start_index > 0:
        btns.append(get_user_button(BACK, NEXT_CMD, start_index - MAX_COUNT_BTN))
    if stop_index < len(users):
        btns.append(get_user_button(NEXT, NEXT_CMD, stop_index))
    keyboard.row(*btns)
    return keyboard
