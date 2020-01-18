from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, GithubUserViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'github-users', GithubUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

