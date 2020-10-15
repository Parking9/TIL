from articles.models import HashTag
from django import template
from articles.models import HashTag
register = template.Library()


@register.filter
def hashtag_link(content):
    lst=[]
    for i in content.split():
        if i.startswith('#')==False:
            lst.append(i)
    return lst

@register.filter
def hashtag_link2(content):
    lst=[]
    for i in content.split():
        if i.startswith('#'):
            hash=HashTag.objects.get(content=i)
            lst.append(hash)
    return lst