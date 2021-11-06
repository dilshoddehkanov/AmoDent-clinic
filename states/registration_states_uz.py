from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalDataUz(StatesGroup):
    id_uz = State()
    first_name_uz = State()
    last_name_uz = State()
    birth_year_uz = State()
    phone_number_uz = State()
    photo_id_uz = State()
