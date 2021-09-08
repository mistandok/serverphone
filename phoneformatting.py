import re


def _get_only_digit(message):
    return re.sub(r'\D', '', message)


def format_phone_num(phone_number):
    phone_number_value = _get_only_digit(phone_number)
    russian_start_numbers = '789'
    allow_number_len = (10, 11)
    phone_pattern = '8 (9{}{}) {}{}{}-{}{}-{}{}'

    if (len(phone_number_value) in allow_number_len and
            phone_number_value[0] in russian_start_numbers):
        if phone_number_value.startswith('9'):
            phone_number_value = '8' + phone_number_value
        phone_number_value = phone_pattern.format(*phone_number_value[2:])

    return phone_number_value