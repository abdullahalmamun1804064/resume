from django import template
register=template.Library()

@register.filter(name='remove_spacial')
def remove_chars(value, arg):
    for charecter in arg:
        value=value.replace(charecter,'')
    return value