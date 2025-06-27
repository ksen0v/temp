import json
import os


def load_config():
    default_config = {
        "token": "your_token",
        "admin_id": 666,
        "min_payup_rub": 180,
        "messages": {
            "startup_admin": "💎 Stitch Roblox | Купить Робуксы 💎\n\nСтатус обновлен: Онлайн 🟢",
            "startup_user": "Алоха! 👋 Ты попал в лучший магазин по Roblox, выберете любую кнопку для продолжения\n\n✨ Средняя оценка: ⭐️⭐️⭐️⭐️⭐️ (~4.97/5)\n\nStitch Roblox желает лучших покупок! ❤️",
            "top_up": "🔥 Напишите желаемое кол-во RUB для покупки!",
            "top_up_proceed": "🖋 Выберите наиболее удобный для вас способ оплаты ⤵️",
            "top_up_by_card": "📩 Отправьте деньги по реквизитам на банковскую карту:\n☎️ Номер: 0000 0000 0000 0000\n\nОтправляйте без комментариев. Получатель Олег Дмитриевич Ж\n\n💰 Оплачиваете: {rub_amount} RUB\n\n📸 После оплаты, отправь сюда, в чат, скриншот оплаты:",
            "bill_photo_need": "❗️ Отправьте нам скриншот чека.",
            "bill_photo_success": "🙌 Отлично! Ваше пополнение на проверке. Она займет не более 1 часа, обычно до 10 минут.",
            "no_money": "⚠️ Недостаточно баланса. На вашем балансе 0 .",
            "no_payout": "❗️ Вывод работает от 100 RBX.",
            "support": "🧑‍💻 Часто задаваемые вопросы:\n\n1. Почему так долго проверяют чек?\n• Чеки проверяются в ручную, а не автоматически. Сотрудники не смогут проверить чек, если вы пополнили в позднее время или раннее вечером. До 24 часов занимает проверка чека.\n\n2. Почему так долго выводят робуксы?\n• Вывод робуксов занимает до 24 часов. Но мы стараемся как можно быстрее вывести вам робуксы. Возможно сотрудник взял перерыв\n\n3. Сколько по времени выводят робуксы?\n• Вывод робуксов происходит до 24 часов от запроса на вывод. Но в большинстве вывод происходит от нескольких минут до часа.\n\n4. Безопасно ли у вас покупать?\n•Весь товар, который продаётся в боте, получен честным путём. Если вы сомневаетесь в безопасности, то лучше покупать в игре.\n\n💡 Прежде чем задать вопрос, убедитесь что здесь нету ответа на ваш вопрос",
            "support_message": "📩 Напишите свой вопрос в поддержку",
            "support_message_success": "Ожидайте, вам ответят в ближайшее время",
            "profile": "📋 Информация о {tag}\nUID: {uid}\n🆔: {id}\n💸 Денег: 0 руб\n🍪 Робуксов: 0 RBX\n\n\nВаша реферальная ссылка - https://t.me/StitchRobloxBot?start=ref-177.\n\n📤 Отправьте её вашим друзьям. Если Ваш друг зарегистрируется по ссылке и купит у нас робаксы, то вы получите процент с его покупок!\n\n👤 У вас 0 рефералов.",
            "rate": "💹 Курс: {rub} за 1 RBX",
            "news": "📰 Наш новостник - t.me/StitchNew\n\n⚠️ Публикуем исключительно важные новости по боту и Robloxу",
            "link_to_news_for_keyboard": "https://t.me/StitchNew",
            "reviews": "😄 Наши отзывы - t.me/stichReviews\n\n💡 Если у вас есть какие-либо сомнения при покупке голды, то вы можете посмотреть отзывы и убедиться в нашей честности.",
            "link_to_reviews_for_keyboard": "https://t.me/StitchNew",
            "buy_gems": "👇 Выбирите количество гемов ниже:",
            "buy_pass": "👇 Выберите Brawl Pass:",
            "min_payup": "Минимальная сумма пополения {amount}",
            "accounts": "Выберите товар: 👇"
        },
        "goods": {
            "gems": {
                "1": "30:199",
                "2": "80:497",
                "3": "110:697",
                "4": "170:997",
                "5": "200:1197",
                "6": "250:1597",
                "7": "360:2197",
                "8": "530:3197",
                "9": "950:4997",
                "10": "2000:9497"
            }
        },
        "accounts": {
            "1": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "1"
            },
            "2": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "2"
            },
            "3": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "3"
            },
            "4": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "4"
            },
            "5": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "5"
            },
            "6": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "6"
            },
            "7": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "7"
            },
            "8": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "8"
            },
            "9": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "9"
            },
            "10": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "10"
            },
            "11": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "11"
            },
            "12": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "12"
            },
            "13": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "13"
            },
            "14": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "14"
            },
            "15": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "15"
            },
            "16": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "16"
            },
            "17": {
                "label": "Названиеss",
                "description": "Описаниеss",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "17"
            },
            "18": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "18"
            },
            "19": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "19"
            },
            "20": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "20"
            },
            "21": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "21"
            },
            "22": {
                "label": "Названиеgg",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "22"
            },
            "23": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "23"
            },
            "24": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "24"
            },
            "25": {
                "label": "Название",
                "description": "Описание",
                "photo1": "media/account_photos/1.jpg",
                "photo2": "media/account_photos/1.jpg",
                "photo3": "media/account_photos/1.jpg",
                "callback": "25"
            }
        }
    }

    if not os.path.exists('config.json'):
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)


config = load_config()
TOKEN = config['token']
ADMIN_ID = config['admin_id']
MESSAGES = config['messages']
MIN_PAYUP_RUB = config['min_payup_rub']
GEMS = config['goods']['gems']
ACCOUNTS = config['accounts']
