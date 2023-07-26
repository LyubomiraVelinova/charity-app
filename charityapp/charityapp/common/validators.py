from django.core.exceptions import ValidationError


def validate_card_verification_value(value):
    if len(value) != 3 or not value.isdigit():
        raise ValidationError('Card verification value must be three digits.')


def validate_card_number(value):
    if len(value) != 16 or not value.isdigit():
        raise ValidationError('Card number must be a 16-digit number.')
