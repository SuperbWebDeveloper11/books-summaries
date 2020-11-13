from django import template
from django.utils.safestring import mark_safe
from taggit.models import Tag
import markdown

register = template.Library()

# markdown filter
@register.filter(name='markdown_format')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

# return all tags or a given number of tags
@register.inclusion_tag('summary/summary/tags_list.html')
def tags_list(num=None):
    if num:
        tags_list = Tag.objects.all()[int(num)]
    else:
        tags_list = Tag.objects.all()
    return {'tags_list': tags_list}
