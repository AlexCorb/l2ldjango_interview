from django import template
import datetime

register = template.Library()

@register.filter(name="l2l_dt")
def l2l_dt(value) :
    """Custom Date Filter"""
    if isinstance(value, datetime.datetime):
        return value
    else:
        return value.replace("T", " ")