from django.views.generic.detail import DetailView
from .models import Book
from .models import Car


class BookDetailView(DetailView):
    model = Book
    template_name = 'ai_app/book_detail.html'  # Określ ścieżkę do swojego szablonu
    context_object_name = 'book'
class CarDetailView(DetailView):
    marka = Car
    template_name='ai_app/car_detail.html'
    context_object_name = 'car'
