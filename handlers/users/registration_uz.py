import sqlite3
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, ContentType

from data.config import ADMINS
from keyboards.default.LanguageKeyboard import contact
from loader import dp, db, bot
from states.registration_states_uz import PersonalDataUz


@dp.message_handler(text='🇺🇿UZ🇺🇿')
@dp.message_handler(commands='uz')
async def language_uz(message: types.Message):
    await message.answer(f'Siz o\'zbek tilini tanladingiz!\n'
                         f'Rus tilini tanlamoqchi bo\'lsangiz /ru ni bosing!\n'
                         f'Botdan foydalanishdan oldin registratsiyadan o\'tishingizni so\'rab qolardik.'
                         f'Registratsiyadan o\'tish uchun esa /registration_uz ni bosing!',
                         reply_markup=ReplyKeyboardRemove())

    await PersonalDataUz.id_uz.set()


@dp.message_handler(commands='registration_uz', state=PersonalDataUz.id_uz)
async def registration(message: types.Message, state: FSMContext):
    await message.answer('‼️‼️‼️Ozgina kuting sizga id berilmoqda...')
    time.sleep(3)

    id_user = message.from_user.id
    await state.update_data(
        {'id_user': id_user}
    )
    await message.answer(f'Sizning id raqamingiz: <b>{id_user}</b>\n\n'
                         f'<i>‼️‼️‼️Bu ma\'lumotni hech kimga bermang. Bu id raqamda sizning shaxsiy ma\'lumotlaringiz joylashgan!</i>')

    await message.answer('Ismingizni kiriting: ')
    await PersonalDataUz.first_name_uz.set()


@dp.message_handler(state=PersonalDataUz.first_name_uz)
async def first_name_uz(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(
        {'first_name': first_name}
    )
    await message.answer('Familiyangizni kiriting: ')
    await PersonalDataUz.last_name_uz.set()


@dp.message_handler(state=PersonalDataUz.last_name_uz)
async def last_name_uz(message: types.Message, state: FSMContext):
    last_name = message.text
    await state.update_data(
        {'last_name': last_name}
    )
    await message.answer('Tug\'ilgan yilingizni kiriting: ')
    await PersonalDataUz.birth_year_uz.set()


@dp.message_handler(state=PersonalDataUz.birth_year_uz)
async def birth_year_uz(message: types.Message, state: FSMContext):
    birth_year = message.text
    await state.update_data(
        {'birth_year': birth_year}
    )
    await message.answer('Telefon raqamizni kiritng: ')
    await PersonalDataUz.phone_number_uz.set()


@dp.message_handler(state=PersonalDataUz.phone_number_uz)
async def phone_number_uz(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(
        {'phone_number': phone_number}
    )

    data = await state.get_data()
    id_user = data.get('id_user')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_year = data.get('birth_year')
    phone_number = data.get('phone_number')

    try:
        db.add_user(
            id_user=id_user,
            first_name=first_name,
            last_name=last_name,
            birth_year=birth_year,
            phone_num=phone_number
        )
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
