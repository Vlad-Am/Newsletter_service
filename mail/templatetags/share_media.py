from django import template


register = template.Library()


@register.filter(name='media_filter')
def media_filter(data):
    if data:
        return f'/media/{data}'
    return '#'
