import base64
from django import template

register = template.Library()

@register.filter
def image_data(image_binary):
    if image_binary:
        return 'data:image/png;base64,' + base64.b64encode(image_binary).decode('utf-8')
    return ''
