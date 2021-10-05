import sqlalchemy.orm
import os
from chronos_bot.database.models import User, Base
from chronos_bot.utils import ChatModes
from chronos_bot.database.db import SessionLocal, engine

Base.metadata.create_all(bind=engine)


bot_token = os.getenv("TOKEN")