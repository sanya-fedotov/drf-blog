import django_filters
from .models import Post, Tag

class PostFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__id',
        to_field_name='id',
        queryset=Tag.objects.all()
    )
    class Meta:
        model = Post
        fields = ['tags']