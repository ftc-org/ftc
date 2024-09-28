from django.urls import path
from update import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
]
