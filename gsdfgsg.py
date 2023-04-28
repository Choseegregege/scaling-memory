import logging
import requests
from aiogram import Bot, Dispatcher, types
from bs4 import BeautifulSoup
import requests
from aiogram.types import ParseMode
from aiogram.dispatcher import filters
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
    keyboard_markup.add(KeyboardButton("Поступление"), KeyboardButton("Информация об обучении"), KeyboardButton("Контакты"), KeyboardButton("Расписание"), KeyboardButton("Новости"))
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
        await bot.send_message(callback_query.from_user.id, 'Чтобы заполнить заявку на поступление "Музыкальное образование" перейдите по ссылке ниже:')
        await bot.send_message(callback_query.from_user.id, 'Музыкальное образование в музыкальном колледже - это специальность, которая готовит студентов к профессиональной музыкальной деятельности. В рамках обучения на этой специальности студенты изучают такие дисциплины, как история музыки, сольфеджио, музыкальная гармония, теория музыки, игра на инструменте, вокал, композиция и аранжировка. Также студенты получают практические навыки в профессиональной музыкальной деятельности, участвуя в концертах и музыкальных проектах, которые организовываются в рамках учебного процесса.\nМузыкальное образование в музыкальном колледже является базовой для дальнейшего обучения на музыкальном факультете в университете и для профессиональной музыкальной карьеры.')
        await bot.send_message(callback_query.from_user.id, 'Заполнить заявку\nпо этой ссылке https://school.muscomplexpavl.edu.kz/index.php/ru/dlya-postupayushchikh')

    elif speciality == 'music_perf':
        await bot.send_message(callback_query.from_user.id, 'Чтобы заполнить заявку на поступление "Инструментальное исполнительство и музыкальное искусство эстрады" перейдите по ссылке ниже:')
        await bot.send_message(callback_query.from_user.id, 'Инструментальное исполнительство - это направление музыкального образования, которое призвано подготовить музыкантов-исполнителей различных инструментов. Обучение включает в себя изучение музыкальной теории, истории музыки, сольфеджио, а также практику игры на инструменте. В зависимости от выбранного инструмента, ученики могут изучать классическую музыку, джаз, рок и другие жанры.\nМузыкальное искусство эстрады - это направление музыкального образования, ориентированное на подготовку исполнителей и композиторов эстрадной музыки. Обучение включает в себя изучение музыкальной теории, композиции, аранжировки, вокала, танца и других аспектов, которые необходимы для успешной работы в индустрии развлечений. Ученики также могут выбрать направление специализации - например, работу с голосом, пение, работу с аранжировками или создание собственных композиций.')
        await bot.send_message(callback_query.from_user.id, 'Заполнить заявку\nпо этой ссылке https://school.muscomplexpavl.edu.kz/index.php/ru/dlya-postupayushchikh')

    elif speciality == 'choir_dir':
        await bot.send_message(callback_query.from_user.id, 'Чтобы заполнить заявку на поступление "Хоровое дирижирование" перейдите по ссылке ниже:')
        await bot.send_message(callback_query.from_user.id, 'Хоровое дирижирование - это одно из направлений музыкального образования, которое предполагает подготовку профессиональных дирижеров хора. Обучение в этой специальности предполагает изучение основ музыкальной теории, истории музыки, пения и звуковедения, а также техники искусства дирижирования.\nСтуденты, обучающиеся на специальности "Хоровое дирижирование", получают практические навыки в работе с хором, изучают технику голосового воспитания и голосового формирования, учатся работать с репертуаром и подбирать музыку, соответствующую возможностям и особенностям коллектива. По окончании обучения студенты могут работать в качестве хоровых дирижеров в различных музыкальных учреждениях, таких как хоры, оркестры, театры и другие. Кроме того, они могут заниматься преподавательской деятельностью в музыкальных школах и колледжах, подготавливая будущих музыкантов и дирижеров.')
        await bot.send_message(callback_query.from_user.id, 'Заполнить заявку\nпо этой ссылке https://school.muscomplexpavl.edu.kz/index.php/ru/dlya-postupayushchikh')

    elif speciality == 'music_theory':
        await bot.send_message(callback_query.from_user.id, 'Чтобы заполнить заявку на поступление "Теория музыки" перейдите по ссылке ниже:')
        await bot.send_message(callback_query.from_user.id, 'Теория музыки - это область знаний, изучающая музыку с точки зрения ее структуры, форм, гармонии, ритма и многих других аспектов. В теории музыки изучаются законы, которые определяют звучание и комбинирование звуков в музыке. Она включает в себя такие темы, как нотная грамота, интервалы, аккорды, модуляции и т.д. Изучение теории музыки является важной частью музыкального образования и помогает музыкантам лучше понимать и анализировать музыкальные произведения, а также создавать свои собственные композиции.')
        await bot.send_message(callback_query.from_user.id, 'Заполнить заявку\nпо этой ссылке https://school.muscomplexpavl.edu.kz/index.php/ru/dlya-postupayushchikh')

    elif speciality == 'vocal':
        await bot.send_message(callback_query.from_user.id, 'Чтобы заполнить заявку на поступление "Пение" перейдите по ссылке ниже:')
        await bot.send_message(callback_query.from_user.id, 'Обучение вокалу в музыкальном колледже предполагает изучение техники пения, репертуара, музыкальной теории и истории вокального искусства. Студенты также могут участвовать в хоровых и ансамблевых проектах, а также имеют возможность выступать на концертах и мероприятиях. Важными аспектами обучения пению являются развитие слуха, дыхания и артикуляции, а также техника произношения и интерпретации музыкальных произведений.')
        await bot.send_message(callback_query.from_user.id, 'Заполнить заявку\nпо этой ссылке https://school.muscomplexpavl.edu.kz/index.php/ru/dlya-postupayushchikh')

   


# Обработчик нажатия на кнопку "Назад в меню"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back_to_menu')
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)


previous_messages = []

# Обработчик команды "Информация об обучении"
@dp.message_handler(lambda message: message.text == "Информация об обучении")
async def process_info_command(message: types.Message):
    text = "Музыкальный колледж - музыкальная школа-интернат для одаренных детей, предоставляющая высококачественное музыкальное образование среднего профессионального уровня. Здесь учатся дети от 6 до 18 лет и обучение включает в себя не только игру на инструментах, но и теоретические знания, вокал и другие музыкальные дисциплины. Одаренные ученики могут получить профессиональное образование и стать музыкантами, певцами, преподавателями музыки и другими специалистами в сфере музыки.\nПродолжение здесь:muscomplexpavl.edu.kz"
    previous_messages.append(await message.answer(text))

# Обработчик команды "Контакты"
@dp.message_handler(lambda message: message.text == "Контакты")
async def process_contacts_command(message: types.Message):
    text = "Наш адрес:\nул.Султанмахмут Торайгырова 67\nТелефон: 8(7182)55-47-17\ne-mail: mus_pav@mail.kz"
    previous_messages.append(await message.answer(text))

@dp.message_handler(lambda message: message.text == "Расписание")
async def process_schedule_command(message: types.Message):
    text = "Расписание доступно по ссылке 1-й семестр: [ссылка](https://drive.google.com/file/d/1Vbek7qfNujfFZlVm2WAIPMFpP7WylLME/view)\nРасписание доступно по ссылке 2-й семестр: [ссылка](https://college.muscomplexpavl.edu.kz/download/uch_vosp_process/2022-2023/2022-23raspisan.pdf)"
    previous_messages.append(await message.answer(text, parse_mode="Markdown"))



# обработчик команды "Новости" в виде кнопки
@dp.message_handler(lambda message: message.text =="Новости")
async def news_command(message: types.Message):
    # парсим HTML-страницу с новостями
    url = "https://college.muscomplexpavl.edu.kz/index.php/ru/174-novosti/2022-iyun/519-2023-aprel-7-v-astane-proshel-pervyj-mezhdunarodnyj-konkurs-qazaq-dumany"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # извлекаем список новостей
    news_items = soup.find_all("div", {"class": "item-page"})
    

    # формируем список строк с новостями
    news_text = []
    for item in news_items:
        title = item.find("h2")
        if title:
            news_text.append(f"<b>{title.text.strip()}</b>\n\n{item.text.strip()}")
    # отправляем новости пользователю
    if news_text:
        await bot.send_message(
            message.chat.id,
            "<b>Новости</b>\n\n" + "\n\n\n".join(news_text),
            parse_mode=ParseMode.HTML,
        )
    else:
        await bot.send_message(message.chat.id, "К сожалению, новостей пока нет.")
        await bot.send_message(message.chat.id, "Для ознакомления с предыдущими новостями, рекомендуется перейти на официальный сайт.:https://college.muscomplexpavl.edu.kz/index.php/ru/")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)