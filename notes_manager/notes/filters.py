from django_filters import rest_framework as filters

from .models import Note


class NotesFilterSet(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter(field_name="date_updated")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    category = filters.CharFilter(field_name="category__name", lookup_expr="iexact")

    class Meta:
        model = Note
        fields = ["is_favorite"]
