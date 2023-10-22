from telebot.util import quick_markup

# def main_menu():
main_menu = quick_markup({
    'Товар 1': {'switch_inline_query': 'start'},
    'Товар 2': {'callback_data': 'whatever'},
    'Товар 3': {'callback_data': 'whatever'},
    'Товар 4': {'callback_data': 'whatever'},
})