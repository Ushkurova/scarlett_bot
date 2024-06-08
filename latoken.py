import re
import private

const_about = "О Латокен"
const_culture = 'Культура'
const_hakaton = 'Хакатон'
const_onboarding = 'Онбординг'

actions =  ['расскажи', 'напиши', 'хочу узнать', 'дай', 'когда', 'что включает', 'из чего состоит', 'что это']

def get_info_character():
    msg = ' Люди которые обладают качествами:\nСверхусилие и ответственность решить проблему, когда большинство сдается\n' \
          'Стресс и давление для ускорения и креативности\n' \
          '“Пытает” коллег до совершенства\n' \
          'Прямота в обсуждении проблем и ошибок, недоработок\n' \
          'Технологии чтобы создать будущее,нежели полировать прошлое'
    return msg

def check_info_character(msg):
    words = ['характер', 'кто работает','какие люди' , 'что нужно']
    extra = ['latoken', 'латокен']
    return check_something_extra(words, extra, msg, False)
def get_info_for_who():
    msg = f'РАБОТА В ЛАТОКЕН ДЛЯ ТЕХНО-ЭНТУЗИАСТОВ СО СПОРТИВНЫМ ХАРАКТЕРОМБыстрый рост через решение нетривиальных задач \n' \
          f'Передовые технологии AIxWEB3\n' \
          f'Глобальный рынок, клиенты в 200+ странах\n' \
          f'Самая успешная компания из СНГ в WEB3\n' \
          f'Удаленная работа, но без дауншифтинга\n' \
          f'Оплата в твёрдой валюте, без привязки к банкам\n' \
          f'Опционы с "откешиванием" криптолетом'
    return msg

def check_for_who(msg):
    words = ['подходит', 'подхожу', 'для кого', 'кто работает', 'могу']
    extra = ['latoken', 'латокен']
    return check_something_extra(words, extra, msg)
def get_info_facts():
    msg = f'1 по числу активов для трейдинга 3,000+ (Бинанс 400+) \n' \
          f'Топ 25 Крипто биржа по рейтингам CoinmarketCap and CoinGecko \n' \
          f'15% аирдропов в мире \n4 миллиона Счетов \n 1 миллион платящих пользователей в 2022'
    return msg

def check_facts(msg):
    words = ['факт']
    extra = ['latoken', 'латокен']
    return check_something_extra(words, extra, msg)
def check_something(items, msg):
    msg_lower = sub_lower(msg)
    for word in items:
        if msg_lower.find(word) != -1:
            for action in actions:
                if msg_lower.find(action) != -1:
                    return True
    return False

def check_something_extra(items, extra, msg, isActions = True):
    msg_lower = sub_lower(msg)
    for word in items:
        if msg_lower.find(word) != -1:
            for action in actions:
                if msg_lower.find(action) != -1 or isActions == False:
                    for ext in extra:
                        if msg_lower.find(ext) != -1:
                            return True
    return False

def check_api_gpt(msg):
    words = ['api', 'апи', 'ключ']
    return check_something(words, msg)


def get_info_name_bot():
    msg = f'Меня зовут Scarlett, я бот из солнечного Шарма. Если у тебя есть еще вопросы ' \
          f'по онбордингу или другим аспектам работы в Latoken, не стесняйся спрашивать! 😊'
    return msg

def get_name(message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    name = first_name
    if name is None:
        name = username
    if name is None:
        name = 'Дорогой пользователь'
    return name

def get_info_culture():
    return get_info_principles() + '\n' + get_info_rules() + '\n' + get_info_ceo()
def get_info_principles():
    msg = f'Latoken имеет уникальную культуру, которая помогает нам быть одними из лучших в своей области. ' \
          f'Вот несколько ключевых аспектов нашей культуры: \n 1. Принципы: \n' \
          f'  - Клиенты на первом месте, эго на последнем: Мы всегда ставим интересы клиентов выше своих собственных. \n' \
          f' - Demo or Die: Мы фокусируемся на результатах и не ищем оправданий. \n' \
          f' - Прозрачность и ответственность: Мы делаем свою работу прозрачной и подотчетной,' \
          f' чтобы устранить халявщиков и решить проблемы. \n  - Открытая обратная связь: ' \
          f'Мы даем честную обратную связь для повышения производительности. \n' \
          f'  - Рост через обратную связь: Мы используем любую обратную связь для роста и никогда не сдаемся.'
    return msg
def get_info_rules():
    msg = f'2. Правила Navy Seals: \n   - Мы работаем в условиях постоянного стресса, хаоса и неудач, ' \
          f'как морские котики, чтобы выявить лидеров.'
    return msg
def get_info_ceo():
    msg = f'3. Peacetime CEO/Wartime CEO: \n   - Wartime CEO: Нарушает протоколы для победы, ' \
          f'фокусируется на деталях и ведет себя агрессивно к конкурентам. \n - Peacetime CEO:' \
          f' Сосредотачивается на большой картине и делегирует решения. \n ' \
          f'Подробнее о нас можно узнать по ссылке: https://deliver.latoken.com/about'
    return msg

def get_info_about():
    msg = f'Latoken — это одна из топ-20 криптобирж и один из топ-20 удаленных работодателей по версии Forbes в 2022 году. ' \
          'Мы предлагаем уникальное сочетание карьерного роста и работы с передовыми технологиями AI и Web3.' \
          ' Latoken — крупнейший супермаркет активов с более чем 19,000 токенов для изучения и 3,000 для торговли.' \
          ' Мы используем AI как копилота для трейдеров, аналитики данных и автоматизации операций. \n ' \
          'Подробнее о нас можно узнать по ссылке: https://deliver.latoken.com/about \n ' \
          'Если у тебя есть еще вопросы, не стесняйся спрашивать!'
    return msg

def get_info_kahaton():
    msg = f' Хакатон Latoken начинается каждую пятницу в 18:00 по московскому времени с презентации ' \
          f'компании и обзора задач. На следующий день, в субботу, участники показывают демо в 18:00, а ' \
          f'победители объявляются в 19:00, после чего следуют интервью и предложения о работе.' \
          f' Призовой фонд хакатона составляет 100K сток опционов за присоединение к компании или 10K LA. \n ' \
          f'Зарегистрироваться можно по ссылке: https://t.me/gpt_web3_hackathon/6694 \n' \
          f'Если у тебя есть еще вопросы, не стесняйся спрашивать!'
    return msg

def check_kahaton(msg):
    words = ['kahaton', 'кахатон']
    return check_something(words, msg)

def check_onboarding(msg):
    words = ['онбординг']
    return check_something(words, msg)

def get_info_onboarding():
    msg = 'Онбординг в Latoken включает несколько ключевых этапов: \n 1. Приветственная встреча:' \
          ' В первый день нового сотрудника приветствуют и знакомят с командой. \n' \
          '2. Обучение и адаптация: Новичок проходит обучение, знакомится с внутренними процессами и инструментами. \n' \
          '3. Менторство: Назначается ментор, который помогает адаптироваться и отвечает на вопросы. \n' \
          '4. Постоянная поддержка: Регулярные встречи с руководителем для обсуждения прогресса и получения обратной связи. \n' \
          'Если у тебя есть еще вопросы, не стесняйся спрашивать!'
    return msg

def sub_lower(msg):
    msg_lower = msg.lower()
    clean_msg = re.sub(r'\s+', ' ', msg_lower).strip()
    return clean_msg


def check_about(msg):
    words = ['latoken', 'латокен']
    return check_something(words, msg)

def check_culture(msg):
    words = ['latoken', 'латокен']
    cultures = ['культур']
    return check_something_extra(words, cultures, msg)

def check_name_bot(msg):
    words = ['как тебя зовут', 'как вас зовут', 'какое у тебя имя', 'твое имя', 'твоё имя']
    msg_lower = sub_lower(msg)
    for text in words:
        if msg_lower.find(text) != -1:
            return True
    return False

def greetings(msg):
    words = ['привет', 'добрый день', 'здравствуйте', 'добрый вечер', 'приветствую тебя']
    msg_lower = sub_lower(msg)
    for text in words:
        if msg_lower==text:
            return True
    return False