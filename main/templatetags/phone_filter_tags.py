# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter()
def phone_format(value):
    if not value:
        return value
    phone_str = str(value)
    if len(phone_str) == 12:
        return f"{phone_str[:3]} ({phone_str[3:6]}) {phone_str[6:8]}-{phone_str[8:10]}-{phone_str[10:12]}"
    return value
