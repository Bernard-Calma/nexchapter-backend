from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]