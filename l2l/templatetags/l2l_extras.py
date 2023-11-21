from django import template
import datetime
import re

register = template.Library()

@register.filter(name="l2l_dt")
def l2l_dt(value) :
    """Custom Date Filter"""
    #return type(value)
    if isinstance(value, datetime.datetime):
        return value
    else:
        return value.replace("T", " ")