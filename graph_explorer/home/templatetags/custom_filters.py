from django import template
import re

register = template.Library()

@register.filter
def parse_filter(filter_query):
    matches = re.findall(r'<(.+?)>', filter_query)
    return [map(str.strip, matches)]