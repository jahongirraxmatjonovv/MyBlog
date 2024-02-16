from django.urls import path
from .views import *
urlpatterns = [    
    path('', main_view, name=''),
#     path('book-create/', bookCreate, name='book-create'),
#     path('book-update/<int:id>/', bookUpdate, name='book-update'),
#     path('book-delete/<int:id>/', bookDelete, name='book-delete'),
#     path('book-detail/', bookDetail, name='book-detail'),
]
