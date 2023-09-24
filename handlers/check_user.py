from dispatcher import bot

async def is_privacy(user_id):
    return (await bot.get_chat(user_id)).username == None