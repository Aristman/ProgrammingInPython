from django import template

register = template.Library()

@register.filter
def inc(a, b):
    return a + b
