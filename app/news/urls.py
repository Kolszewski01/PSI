from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, CommentViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
