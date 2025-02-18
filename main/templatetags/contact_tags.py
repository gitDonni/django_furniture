from django import template
from main.models import ContactInfo


register = template.Library()


@register.simple_tag()
def tag_contacts():
    return ContactInfo.objects.all()
