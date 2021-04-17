from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import bs
import random
import time

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    
    title1 = ''
    while True:
    	a = random.randint(5,10)
    	title = bs.post_list()
    	
    	if title1 == title:
    		time.sleep(a)
    		
    	else:
    		await bot.send_message(msg.from_user.id, title)
    		title1 = title
    		time.sleep(a)
    		

if __name__ == '__main__' :
	executor.start_polling(dp, skip_updates=True)

'''
Один раз пишешь старт и отвечает всегда:
executor.start_polling(dp)

Отвечает только при старт:
executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
'''