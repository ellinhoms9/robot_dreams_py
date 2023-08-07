from django.urls import path
from book import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-list'),
    path('<int:pk>', views.BookDetailView.as_view(), name='books-detail'),
    path('create/', views.BooksCreateView.as_view(), name='books-create')
]
