from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, AuthorViewSet, BookViewSet, ReviewViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]