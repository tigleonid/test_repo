from django import template
from main.other.markdown import generate_html

register = template.Library()


@register.filter
def to_str(value):
    return str(value)


register.filter(generate_html)
