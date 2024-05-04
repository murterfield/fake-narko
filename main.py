from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

import config
from config import API_TOKEN
from scripts import keyboards
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(text=['/start'])
async def send_welcome(message: types.Message):
    await message.answer( f"🔸Добро пожаловать {message.from_user.username}! \n 🔸Создатель бота - SCAR3CROW",
                          reply_markup=keyboards.keyboard1 )


@dp.message_handler(text=['🔻Купить'])
async def choose_city(message: types.Message):
    await message.answer("🧊 Выбери свой город 🧊", reply_markup=keyboards.keyboard2() )

@dp.message_handler(text=['💰Пополнить баланс'])
async def choose_city(message: types.Message):
    await message.answer(f"👤 {message.from_user.username}, \n \n Ваш балланс:        *0.00р* \n \n 🔸 Перевод по карте: `{config.card}`  \n \n 🔸 Перевод по киви: `{config.qiwi}` \n \n 🔸 Перевод по btc: `{config.bitcoin}` \n \n ▪️ В комментарии напишите свой юзер-нейм \n \n ▪️ И в течении 5 минут после проверки модерации \n \n ▪️ Деньги придут вам на балланс", parse_mode='Markdown')

@dp.message_handler(text=['☎️Поддержка'])
async def choose_city(message: types.Message):
    await message.answer(F'{config.tp}')

@dp.message_handler(text=['👤О нас'])
async def choose_city(message: types.Message):
    await message.answer(F'{config.AboutUS}')

@dp.message_handler(text=['📜Правила'])
async def choose_city(message: types.Message):
    await message.answer(F'{config.rules}')

@dp.callback_query_handler(text='msk')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔹 Выбери товар 🔹", reply_markup=keyboards.keyboard3())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='spb')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔹 Выбери товар 🔹", reply_markup=keyboards.keyboard4())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='ekb')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔹 Выбери товар 🔹", reply_markup=keyboards.keyboard5())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='udom')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔹 Выбери товар 🔹", reply_markup=keyboards.keyboard6())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='sochi')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔹 Выбери товар 🔹", reply_markup=keyboards.keyboard7())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='shishki')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 1500р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='sol')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 2300р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='mef')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 1890р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='gashish')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 1650р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='ext')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 2000р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='cox')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Выбери фасовку 🔹 \n 🥀 Если 1г стоит 3400р", reply_markup=keyboards.buy())
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

@dp.callback_query_handler(text='buy1')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"🔹 Подтвердите покупку 🔹", reply_markup=keyboards.buy1())
    # Удаляем прошлое сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


@dp.callback_query_handler(text='error')
async def msk_prod(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f"⚠️ Недостаточно средств для оплаты! ⚠️ n 💲 Вы можете пополнить баланс прямо сейчас 💲")
    # Удаляем прошлое сообщение
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
