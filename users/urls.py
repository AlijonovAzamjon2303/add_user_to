from django.urls import path
from .views import view, home  # success_view ni keyin quyida yaratamiz

urlpatterns = [
    path('', view, name='add'),
]
