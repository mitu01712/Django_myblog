from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def get_recent_posts(count=5):
    return Post.objects.filter(status='Published').order_by('-created_at')[:count]