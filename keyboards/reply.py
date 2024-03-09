from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(
    *btns: str,
    placeholder: str = None,
    request_contact: int = None,
    request_location: int = None,
    sizes: tuple[int] = (2,),
):
    '''
    Parameters request_contact and request_location must be as indexes of btns args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",            
            placeholder="Команды перед Вами!",
            request_contact=2,  # index of "Варианты оплаты" button
            sizes=(2, 2, 1)
        )
    '''
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):
        
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:

            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
            resize_keyboard=True, input_field_placeholder=placeholder)



start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Показать меню"),
            KeyboardButton(text="Информация о магазине"),
        ],
        [
            KeyboardButton(text="Способы оплаты"),
            KeyboardButton(text="Информация о доставке"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Сделай свой выбор!",
)

del_keyboard = ReplyKeyboardRemove()

start_keyboard2 = ReplyKeyboardBuilder()
start_keyboard2.add(
    KeyboardButton(text="Показать меню"),
    KeyboardButton(text="Информация о магазине"),
    KeyboardButton(text="Способы оплаты"),
    KeyboardButton(text="Информация о доставке"),
)
start_keyboard2.adjust(2, 2)

start_keyboard3 = ReplyKeyboardBuilder()
start_keyboard3.attach(start_keyboard2)
start_keyboard2.row(KeyboardButton(text="Оставить отзыв"))

test_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос", 
                           request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Отправить номер", request_contact=True),
            KeyboardButton(text="Отправить место", request_location=True),
        ],
    ]
)
