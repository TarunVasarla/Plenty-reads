import django_filters
from .models import Book
class BookListFilter(django_filters.FilterSet):
    # book_fltr = django_filters.CharFilter('Book__bookname')
    Book.objects.filter(name__icontains=search_word)
    class Meta:
        model = Book
        fields = ['bookname', 'AuthorName', 'preface','genre','uploadBook'] 