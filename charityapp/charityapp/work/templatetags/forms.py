from django import template

register = template.Library()


@register.filter
def placeholder(field, token):
    field.field.widget.attrs['placeholder'] = token

    return field


# Adding custom class
# @register.filter
# def form_field_class(form_field, className):
#     form_field.field.widget.attrs['class'] = className
#
#     return form_field
