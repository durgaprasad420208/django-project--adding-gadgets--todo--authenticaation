from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gadget-list/', views.gadget_list, name='list'),
    path('add-gadgets/', views.add_gadgets, name='add'),
    path('add-brand/', views.add_brand, name='brand'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
