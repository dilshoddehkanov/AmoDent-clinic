from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from keyboards.default.LanguageKeyboard import language
from states.registration_states_uz import PersonalDataUz


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!"
                         f"AmoDent klinikasining rasmiy botiga xush kelibsiz!!!\n\n")
    await message.answer('Tilni tanlang👇👇👇', reply_markup=language)





@dp.message_handler(text='🇷🇺RU🇷🇺')
@dp.message_handler(commands='ru')
async def language_uz(message: types.Message):
    await message.answer(f'Вы выбрали русский язык!\n'
                         f'Если вы хотите выбрать узбекский язык, нажмите /uz!\n'
                         f'Мы просим вас зарегистрироваться перед использованием бота\n'
                         f'Чтобы зарегистрироваться, нажмите /registration_ru!', reply_markup=ReplyKeyboardRemove())
