import private, gpt, latoken
from telebot import types


@private.scarlett.message_handler(commands=["start"])
def start (message):
    msg = f'{latoken.get_name(message)}, приветствую тебя'
    keyboard = types.ReplyKeyboardMarkup( resize_keyboard=True)
    about = types.KeyboardButton(text=latoken.const_about)
    culture = types.KeyboardButton(text=latoken.const_culture)
    hakaton = types.KeyboardButton(text=latoken.const_hakaton)
    onboarding = types.KeyboardButton(text=latoken.const_onboarding)
    keyboard.add(about, culture, hakaton, onboarding)
    private.scarlett.send_message(message.chat.id, msg, reply_markup=keyboard)

@private.scarlett.message_handler(content_types=["text"])
def start (message):
    if message.text == latoken.const_culture or latoken.check_culture(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_culture()}'
    elif message.text == latoken.const_hakaton or latoken.check_kahaton(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_kahaton()}'
    elif message.text == latoken.const_about or latoken.check_about(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_about()}'
    elif message.text == latoken.const_onboarding or latoken.check_onboarding(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_onboarding()}'
    elif latoken.check_name_bot(message.text) or latoken.greetings(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_name_bot()}'
    elif latoken.check_api_gpt(message.text):
        msg = f'{latoken.get_name(message)},{private.scarlett}'
    elif latoken.check_facts(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_facts()}'
    elif latoken.check_for_who(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_for_who()}'
    elif latoken.check_info_character(message.text):
        msg = f'{latoken.get_name(message)},{latoken.get_info_character()}'
    else:
        msg = gpt.get_answer_gpt(message.text)

    private.scarlett.send_message(message.chat.id, msg)


private.scarlett.polling(none_stop=True)
