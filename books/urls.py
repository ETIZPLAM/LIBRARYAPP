from django.urls import path
from books import views


urlpatterns=[
    path('post-books/', views.post_books)
]