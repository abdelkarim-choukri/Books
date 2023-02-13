from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.html import escape        
from django.contrib.auth import get_user_model
import logging
from django import template
register = template.Library()



@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">',extra_classes)

@register.simple_tag
def endcol():
    return format_html("</div>")