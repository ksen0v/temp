from aiogram.types import FSInputFile, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_loader import MESSAGES, GEMS, ACCOUNTS
from core.pagiantion import Pagination


def top_up_by_card_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💰 Банковской картой', callback_data='top_up_by_card')
    keyboard.adjust(1)

    return keyboard.as_markup()


def popup_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💳 Пополнить', callback_data='top_up_by_card_two')
    keyboard.adjust(1)

    return keyboard.as_markup()


def contact_support_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='✉️ Связаться', callback_data='contact_support')
    keyboard.adjust(1)

    return keyboard.as_markup()


def main_menu_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🏠 Главное меню', callback_data='main_menu')
    keyboard.adjust(1)

    return keyboard.as_markup()


def news_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📰 Перейти в новостник', url=str(MESSAGES['link_to_news_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()


def reviews_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='😄 Отзывы', url=str(MESSAGES['link_to_reviews_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()


def buy_gems_inline():
    keyboard = InlineKeyboardBuilder()
    for i in range(10):
        lot = str(GEMS[f"{i + 1}"]).split(':', 1)
        keyboard.button(text=f'Fortnite {lot[0]} V-Баксов | {lot[1]} ₽', callback_data='no_money')
    keyboard.adjust(1)

    return keyboard.as_markup()


def buy_pass_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f'Боевой пропуск | 399 руб', callback_data='no_money')
    keyboard.button(text=f'Стартер пак «Мир грёз» | 229 руб', callback_data='no_money')
    keyboard.adjust(1)

    return keyboard.as_markup()


def buy_accounts_inline(page=0):
    keyboard = InlineKeyboardBuilder()

    start_offset = page*5
    end_offset = start_offset + 5

    for i in range(start_offset, end_offset):
        account = ACCOUNTS[f"{i + 1}"]
        keyboard.row(InlineKeyboardButton(text=account['label'], callback_data=f"account_{account['callback']}"))

    btns_row = []
    if page > 0:
        btns_row.append(InlineKeyboardButton(
            text="⬅️",
            callback_data=Pagination(page=page - 1).pack(),
        )
        )
    if end_offset < 25:
        btns_row.append(
            InlineKeyboardButton(
                text="➡️",
                callback_data=Pagination(page=page + 1).pack(),
            )
        )

    keyboard.row(*btns_row)

    return keyboard.as_markup()


def account_buy_inline():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="💳 КУПИТЬ", callback_data="no_money")
    keyboard.adjust(1)

    return keyboard.as_markup()