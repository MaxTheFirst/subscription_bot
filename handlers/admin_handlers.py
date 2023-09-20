from config import DATA_FORMAT
from dispatcher import dp, bot
from states import UserStates
from db import DBManager
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from datetime import datetime
import texts
import keyboards


@dp.message_handler(commands=[texts.START_COMMAND], commands_prefix=texts.PREFIX, state=None, is_admin=True)
async def on_start_admin(message: Message):
    await message.answer(texts.ADMIN_TEXT)


async def get_user_from(message: Message, args):
    user_id = int(args[0])
    user = DBManager.get_user(user_id)
    if not user:
        await message.answer(texts.ERROR)
        return None
    await message.delete_reply_markup()
    return user


@dp.callback_query_handler(callback_cmd=texts.UPDATE_KEY)
async def update_click(callback: CallbackQuery, state: FSMContext, args):
    user = await get_user_from(callback.message, args)
    if user:
        await callback.message.answer(texts.UPDATE_TEXT.format(user.finish_sub.strftime(DATA_FORMAT)))
        await state.update_data(user_id=user.user_id)
        await UserStates.paste_date.set()


@dp.message_handler(state=UserStates.paste_date)
async def read_date(message: Message, state: FSMContext):
    try:
        now = datetime.now().date()
        next_date = datetime.strptime(message.text, DATA_FORMAT).date()
        if next_date > now:
            user_id = (await state.get_data())['user_id']
            DBManager.update_user(user_id, finish_sub=next_date)
            await message.answer(texts.UPDATE_OK)
            await state.finish()
            await bot.send_message(user_id, texts.USER_UPDATE_TEXT.format(next_date.strftime(DATA_FORMAT)))
            return
    except ValueError:
        pass
    await message.answer(texts.ERROR)


@dp.message_handler(commands=[texts.LIST_COMMAND], commands_prefix=texts.PREFIX, state=[*UserStates.all_states, None], is_admin=True)
async def view_list(message: Message):
    users = DBManager.users()
    if users:
        text = texts.LIST_TEXT
        for user in users:
            text += f'\n{user.fi_name} - {user.finish_sub.strftime(DATA_FORMAT)}'
    else:
        text = texts.NO_USERS
    await message.answer(text)


@dp.message_handler(commands=[texts.UPDATE_COMMAND], commands_prefix=texts.PREFIX, state=[*UserStates.all_states, None], is_admin=True)
async def update_choose(message: Message):
    keyboard = keyboards.get_users_keyboard()
    if keyboard:
        await message.answer(texts.CHOOSE_USER, reply_markup=keyboard)
    else:
        await message.answer(texts.NO_USERS)


@dp.callback_query_handler(callback_cmd=texts.NEXT_CMD)
async def edit_keyboard(callback: CallbackQuery, args):
    keyboard = keyboards.get_users_keyboard(int(args[0]))
    if keyboard:
        await callback.message.edit_reply_markup(keyboard)


@dp.callback_query_handler(callback_cmd=texts.CHOOSE_KEY)
async def choose_user(callback: CallbackQuery, args):
    user = await get_user_from(callback.message, args)
    if user:
        keyboard = keyboards.get_admin_keyboard(user.user_id, True)
        await callback.message.answer(texts.EDIT_TEXT.format(user.fi_name, user.finish_sub.strftime(DATA_FORMAT)), reply_markup=keyboard)


@dp.callback_query_handler(callback_cmd=texts.DELETE_CMD)
async def choose_user(callback: CallbackQuery, args):
    DBManager.delete_user(int(args[0]))
    await callback.message.answer(texts.DELETE_OK)