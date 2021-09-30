import os

from gestione_bot.database.db import SessionLocal
from enum import Enum
import random
import string
import requests


def get_db():
    with SessionLocal() as ses:
        yield ses


class ChatModes(Enum):
    NONE = 0