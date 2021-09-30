import sqlalchemy.orm
import telepot
import asyncio
import os
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
from gestione_bot.database.models import User, Base
from gestione_bot.utils import ChatModes
from gestione_bot.database.db import SessionLocal, engine

Base.metadata.create_all(bind=engine)


class CharonProgram(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(CharonProgram, self).__init__(*args, **kwargs)
        self.mode = ChatModes.NONE

    async def private_chat_handler(self, msg):
        pass

    async def on_chat_message(self, msg):
        if msg['chat']['type'] == "private":
            await self.private_chat_handler(msg)
        else:
            await self.public_chat_handler(msg)

    async def on_close(self, ex):
        pass


bot_token = os.getenv("TOKEN")

bot = telepot.aio.DelegatorBot(bot_token, [pave_event_space()(per_chat_id(), create_open, CharonProgram, timeout=120)])
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print("Bot is running...")
loop.run_forever()