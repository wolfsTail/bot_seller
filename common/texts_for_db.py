from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Букеты', 'Корзины']

description_for_info_pages = {
    "main": "Добро пожаловать!",
    "about": "Продажа цветов и иных композиций.\nРежим работы - круглосуточно.",
    "payment": as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При получении карта/кеш",        
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовывоз (сейчас прибегу заберу)",            
            marker="✅ ",
        ),
        as_marked_section(Bold("Нельзя:"), "Почта Росии", "Транспортные компании", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Категории:',
    'cart': 'Корзина пуста'
}