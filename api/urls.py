from django.urls import include, path
from api.views import EventViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
