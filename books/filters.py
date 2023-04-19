import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='iexact')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='iexact')
    pub_date_from = django_filters.DateFilter(field_name='publication_date', lookup_expr='gte')
    pub_date_to = django_filters.DateFilter(field_name='publication_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['genre', 'author', 'pub_date_from', 'pub_date_to']