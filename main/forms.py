from django.core.exceptions import ValidationError


def phone_number_validator(phone_number):
    if phone_number.startswith('+375') and (phone_number[4:6] in ['25', '29', '33', '44']):
        print('All right')
        return phone_number
    else:
        print('Wrong number')
        raise ValidationError('Неправильный номер телефона')