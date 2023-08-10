from django.core.exceptions import ValidationError


def validate_card_verification_value(value):
    if len(value) != 3 or not value.isdigit():
        raise ValidationError('Card verification value must be three digits.')


def validate_card_number(value):
    if len(value) != 16 or not value.isdigit():
        raise ValidationError('Card number must be a 16-digit number.')


def validate_phone(value):
    if value is None:
        raise ValidationError("Phone cannot be None")

    if not value.startswith('0') and not value.startswith('+'):
        raise ValidationError("Phone must starts with '0' or '+'")
