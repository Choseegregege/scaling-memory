import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# Инициализация бота
API_TOKEN = '6019567634:AAE-pSGL3UF9B7cv85rebSj8hX6pketiFGk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Инициализация логгера
logging.basicConfig(level=logging.INFO)

# Функция для обработки команды /start
@dp.message_handler(text="/start")
async def back_to_menu(message: types.Message):
    keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_markup.add(KeyboardButton("Поступление"), KeyboardButton("Информация об обучении"), KeyboardButton("Контакты"), KeyboardButton("Расписание"))
    await message.answer("Добро пожаловать в музыкальный комплекс \"Музыкальный колледж - музыкальная школа-интернат для одаренных детей\"! Чем могу помочь?", reply_markup=keyboard_markup)

# Функция для обработки нажатия кнопки "Назад"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back_to_menu')
async def process_callback_back_to_menu(callback_query: types.CallbackQuery):
    keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_markup.add(KeyboardButton("Поступление"), KeyboardButton("Информация об обучении"), KeyboardButton("Контакты"), KeyboardButton("Расписание"))
    await bot.send_message(callback_query.from_user.id, "Чем могу помочь?", reply_markup=keyboard_markup)



# Функция для обработки кнопки "Поступление"
@dp.message_handler(lambda message: message.text == "Поступление")
async def process_admission_command(message: types.Message):
    keyboard_markup = InlineKeyboardMarkup()
    keyboard_markup.row(InlineKeyboardButton("Музыкальное образование", callback_data='music_edu'))
    keyboard_markup.row(InlineKeyboardButton("Инструментальное исполнительство и музыкальное искусство эстрады", callback_data='music_perf'))
    keyboard_markup.row(InlineKeyboardButton("Хоровое дирижирование", callback_data='choir_dir'))
    keyboard_markup.row(InlineKeyboardButton("Теория музыки", callback_data='music_theory'))
    keyboard_markup.row(InlineKeyboardButton("Пение", callback_data='vocal'))
    await message.answer("Выберите желаемую специальность", reply_markup=keyboard_markup)



@dp.callback_query_handler(lambda callback_query: True)
async def process_callback(callback_query: types.CallbackQuery):
    speciality = callback_query.data

    await bot.answer_callback_query(callback_query.id)

    if speciality == 'music_edu':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали "Музыкальное образование". Введите свои данные для записи на прослушивания: ФИО, дата рождения, номер телефона и email.')
        keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

    elif speciality == 'music_perf':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали "Инструментальное исполнительство и музыкальное искусство эстрады". Введите свои данные для записи на прослушивания: ФИО, дата рождения, номер телефона и email.')
        keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

    elif speciality == 'choir_dir':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали "Хоровое дирижирование". Введите свои данные для записи на прослушивания: ФИО, дата рождения, номер телефона и email.')
        keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

    elif speciality == 'music_theory':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали "Теория музыки". Введите свои данные для записи на прослушивания: ФИО, дата рождения, номер телефона и email.')
        keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

    elif speciality == 'vocal':
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали "Пение". Введите свои данные для записи на прослушивания: ФИО, дата рождения, номер телефона и email.')
        keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))

    # Добавляем кнопку "Назад в меню" после отправки сообщения с выбором специальности
    back_to_menu_button = types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu')
    keyboard = types.InlineKeyboardMarkup(row_width=1).add(back_to_menu_button)
    


# Обработчик нажатия на кнопку "Назад в меню"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back_to_menu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)


previous_messages = []

# Обработчик команды "Информация об обучении"
@dp.message_handler(lambda message: message.text == "Информация об обучении")
async def process_info_command(message: types.Message):
    text = "Данный музыкальный комплекс предлагает обучение детей и подростков с 6 до 17 лет. В комплексе доступны следующие инструменты для обучения: Музыкальное образование, Инструментальное исполнительство и музыкальное искусство эстрады, Хоровое дирижирование, Ударные инструменты, Теория музыки, Пение. Все преподаватели имеют высшее музыкальное образование и опыт преподавания.\nПродолжение здесь:muscomplexpavl.edu.kz"
    previous_messages.append(await message.answer(text))

# Обработчик команды "Контакты"
@dp.message_handler(lambda message: message.text == "Контакты")
async def process_contacts_command(message: types.Message):
    text = "Наш адрес:\nул.Султанмахмут Торайгырова 67\nТелефон: 8(7182)55-47-17\ne-mail: mus_pav@mail.kz"
    previous_messages.append(await message.answer(text))

# Обработчик команды "Расписание"
@dp.message_handler(lambda message: message.text == "Расписание")
async def process_schedule_command(message: types.Message):
    text = "Расписание доступно по ссылке 1-й семестр: https://drive.google.com/file/d/1Vbek7qfNujfFZlVm2WAIPMFpP7WylLME/view\nРасписание доступно по ссылке 2-й семестр: https://college.muscomplexpavl.edu.kz/download/uch_vosp_process/2022-2023/2022-23raspisan.pdf"
    previous_messages.append(await message.answer(text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
