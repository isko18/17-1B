from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет Студент !")
    
@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу помочь?")
    
@dp.message_handler(commands='geeks')
async def geeks(message:types.Message):
    await message.reply("Приходи на курсы!")

@dp.message_handler(lambda message: message.text.lower() == 'привет')
async def hello(message:types.Message):
    await message.reply("Привет как дела?")    
    
@dp.message_handler(commands='photo')
async def photo(message:types.Message):
    await message.answer_photo("https://www.actuia.com/wp-content/uploads/2022/01/logopython-768x333.png")
    
@dp.message_handler(commands='location')
async def location(message:types.Message):
    await message.answer_location(40.5134883, 72.8153475)
    
@dp.message_handler(commands='contact')
async def contact(message:types.Message):
    last_name = "Isko"
    first_name = "geeks"
    number = +996505180600
    await message.answer_contact(last_name=last_name, first_name=first_name, phone_number=number)

executor.start_polling(dp)
