from django.urls import path
from . import views

urlpatterns = [
    path('add-to-ommon-list/', views.add_to_common_list_view),
]