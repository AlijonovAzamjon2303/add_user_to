from django.urls import path
from .views import view, home_view  # success_view ni keyin quyida yaratamiz

urlpatterns = [
    path('', view, name='add'),
    path('users/', home_view, name='users'),
]
