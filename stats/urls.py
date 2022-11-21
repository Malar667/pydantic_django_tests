from rest_framework.routers import DefaultRouter

from stats.views import AuthorDjanticViewSet, AuthorViewSet

router = DefaultRouter()

router.register(r"drf", AuthorViewSet, basename="drf")
router.register(r"djantic", AuthorDjanticViewSet, basename="djantic")

urlpatterns = router.urls
