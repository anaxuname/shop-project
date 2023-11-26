from django import template

register = template.Library()


@register.filter()
@register.simple_tag()
def mediapath(val):
    if not val:
        return ''
    return "/media/" + str(val)
