class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.name) for x in cls)
