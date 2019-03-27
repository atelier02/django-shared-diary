#以下から引用
#https://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables
#https://torina.top/detail/294/

from urllib.parse import urlencode
from django import template

register = template.Library()

# @register.simple_tag(takes_context=True)
# def url_replace(context, **kwargs):
#     query = context['request'].GET.dict()
#     query.update(kwargs)
#     return urlencode(query)

@register.simple_tag
def url_replace(request, value):
    dict_ = request.GET.copy()
    dict_["page"] = value
    return dict_.urlencode()
