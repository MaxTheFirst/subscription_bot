from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    paste_name = State()
    pay = State()
    paste_date = State()