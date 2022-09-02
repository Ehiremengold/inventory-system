from django.urls import path
from .views import (index, display_laptops, display_desktops,
                    display_mobile, add_laptop, add_mobile,
                    add_desktop, edit_desktop, edit_laptop,
                    edit_mobile, delete_desktop, delete_laptop, delete_mobile)

urlpatterns = [
    path('', index, name='index'),
    path('Laptops/', display_laptops, name='laptops'),
    path('Desktops/', display_desktops, name='desktops'),
    path('Mobiles/', display_mobile, name='mobile'),
    path('add_laptop/', add_laptop, name="add_laptop"),
    path('add_mobile/', add_mobile, name="add_mobile"),
    path('add_desktop/', add_desktop, name="add_desktop"),
    path('edit_laptop/<int:pk>/', edit_laptop, name="edit_laptop"),
    path('edit_mobile/<int:pk>/', edit_mobile, name="edit_mobile"),
    path('edit_desktop/<int:pk>/', edit_desktop, name="edit_desktop"),
    path('delete_laptop/<int:pk>/', delete_laptop, name='delete_laptop'),
    path('delete_desktop/<int:pk>/', delete_desktop, name='delete_desktop'),
    path('delete_mobile/<int:pk>/', delete_mobile, name='delete_mobile'),
]
