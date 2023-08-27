from django import template

register = template.Library()


@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter
def active_version(val):
    version = 'Не установлена'
    if val:
        for item in val:
            if item.is_active:
                version = item
            else:
                continue
    return version
