from django import template

register = template.Library()


@register.filter
def percentage_complete(current_amount, goal_amount):
    if goal_amount == 0:
        return 0
    return int((current_amount / goal_amount) * 100)
