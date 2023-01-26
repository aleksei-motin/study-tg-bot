# -*- coding: utf8 -*-

from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
import time as t
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from api_token import API_TOKEN
import datetime as dt


storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)
