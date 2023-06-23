from django import template

register = template.Library()

@register.filter(name='remove_spacial')
def remove_chars(value):
    # Remove any special characters from the value
    value = value.replace('[', '').replace(']', '').replace("'", '')
    return value

@register.filter(name='add_comma')
def add_comma(value):
    # Add a comma after each city
    value = value.replace(' ', ', ')
    return value
