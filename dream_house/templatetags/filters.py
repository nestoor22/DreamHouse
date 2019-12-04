from django import template

register = template.Library()


@register.filter(name='add_css_class')
def add_class(value, class_name):
    return value.as_widget(attrs={'class': class_name})