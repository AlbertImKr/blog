from django import template

register = template.Library()


@register.filter
def random_text_bg_color(value):
    colors = ['text-bg-warning', 'text-bg-danger', 'text-bg-info',
              'text-bg-primary', 'text-bg-success',
              'text-bg-success', 'text-bg-info', 'text-bg-light',
              'text-bg-dark', 'text-bg-white']

    concatenated_numbers = ''.join(str(ord(char)) for char in value)
    number = int(concatenated_numbers)
    index = number % len(colors)

    return colors[index]


@register.filter
def random_bg_color(value):
    colors = ['bg-warning', 'bg-danger', 'bg-info',
              'bg-primary', 'bg-success',
              'bg-success', 'bg-info', 'bg-light',
              'bg-dark', 'bg-white']
    concatenated_numbers = ''.join(str(ord(char)) for char in value)
    number = int(concatenated_numbers)
    index = number % len(colors)
    return colors[index]


@register.filter
def random_text_color(value):
    colors = ['text-warning', 'text-danger', 'text-info',
              'text-primary', 'text-success',
              'text-success', 'text-info', 'text-light',
              'text-dark', 'text-white']
    concatenated_numbers = ''.join(str(ord(char)) for char in value)
    number = int(concatenated_numbers)
    index = number % len(colors)
    return colors[index]
