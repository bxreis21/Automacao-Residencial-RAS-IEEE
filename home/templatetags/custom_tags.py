from django import template
 
register = template.Library()

@register.filter(name='color_status')
def color_status(value: bool) -> str:
    if value:
        return 'green'
    return 'red'

@register.filter(name='string_status')
def string_status(value: bool) -> str:
    if value:
        return 'Ativado'
    return 'Desativado'