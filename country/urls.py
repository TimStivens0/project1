from django.urls import path
from .views import home_view, input_view, update_view, delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('input/', input_view, name='input'),
    path('update/<int:id>/', update_view, name='update'),
    path('delete/<int:id>/', delete_view, name='delete'),
]