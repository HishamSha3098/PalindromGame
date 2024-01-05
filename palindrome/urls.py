# palindrome/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GameViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('games/<int:pk>/getBoard/', GameViewSet.as_view({'get': 'getBoard'}), name='game-get-board'),
    path('games/<int:pk>/updateBoard/', GameViewSet.as_view({'post': 'updateBoard'}), name='game-update-board'),
]
