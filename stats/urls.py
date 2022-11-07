from rest_framework.routers import DefaultRouter

from stats.models import Author
from stats.views import AuthorDjanticViewSet, AuthorViewSet

router = DefaultRouter()

router.register(r"serializer", AuthorViewSet, basename=Author)
router.register(r"djantic", AuthorDjanticViewSet, basename=Author)

urlpatterns = router.urls
