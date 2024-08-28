import random

from django import template

register = template.Library()


@register.filter
def random_text_bg_color(category):
    colors = ['text-bg-warning', 'text-bg-danger', 'text-bg-info',
              'text-bg-primary', 'text-bg-success', 'text-bg-secondary',
              'text-bg-success', 'text-bg-info', 'text-bg-light',
              'text-bg-dark', 'text-bg-white']

    concatenated_numbers = ''.join(str(ord(char)) for char in category.name)
    number = int(concatenated_numbers)
    index = number % len(colors)

    return colors[index]


@register.filter
def random_bg_color():
    colors = ['bg-warning', 'bg-danger', 'bg-info',
              'bg-primary', 'bg-success', 'category_filters',
              'bg-success', 'bg-info', 'bg-light',
              'bg-dark', 'bg-white', 'bg-muted']
    return random.choice(colors)
