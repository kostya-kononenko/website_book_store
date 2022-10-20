"""World_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog/books/', views.BookListView.as_view(), name='books'),
    path('catalog/books/<int:pk>', views.BookDetailView.as_view(), name='books-detail'),
    path('catalog/books/mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('catalog/authors/', views.AuthorLIstView.as_view(), name='authors'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
]
