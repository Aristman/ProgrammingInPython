from django import template

register = template.Library()


@register.filter
def inc(a, b):
    try:
        return str(int(a) + int(b))
    except ValueError:
        return None


@register.simple_tag
def division(a, b, to_int=False):
    try:
        a = int(a)
        b = int(b)
        return str(int(a / b)) if to_int == True else str(a / b)
    except Exception:
        return None