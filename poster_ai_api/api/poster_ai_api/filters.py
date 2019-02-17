import django_filters
from rest_framework import filters
from api.poster_ai_api.models import Face

class FaceFilter(django_filters.FilterSet):
  # set lookup_expr='contain' to filter by YYYY-MM-DD or comment date assignment for exact
  # date = django_filters.DateFilter(name='date')

  class Meta:
    model = Face
    fields = ['session_id', 'poster_id']