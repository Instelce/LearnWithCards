from atexit import register
from django import template
from django.template.defaultfilters import stringfilter
import markdown


register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return markdown.markdown(value, extensions=['markdown.extensions.fenced_code'])
