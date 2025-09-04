from api.views import StudentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')
urlpatterns = router.urls
