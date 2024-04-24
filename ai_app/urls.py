from django.urls import path
from .views import BookDetailView
from .views import CarDetailView

# Lista `urlpatterns` definiuje wzorce URL dla aplikacji, przypisując konkretne ścieżki URL do widoków.
urlpatterns = [
    # Definicja pojedynczego wzorca URL:
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('car/<int:pk>/', CarDetailView.as_view(),name='car-detail'),
]