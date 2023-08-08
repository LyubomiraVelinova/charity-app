from django import template

register = template.Library()


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def verbose_name_from_object(obj, field_name):
    model = obj._meta.model
    field = model._meta.get_field(field_name)
    return field.verbose_name
