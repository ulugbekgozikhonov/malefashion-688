from django.core.exceptions import ValidationError


def rating_validation(value):
    if not (1 <= value <= 5):
        raise ValidationError('Rating must be between 1 and 5',
                              params={"value": value}
                              )
