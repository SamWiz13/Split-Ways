from rest_framework.routers import DefaultRouter
from .views import LoginView


router = DefaultRouter()

router.register(r'auth',LoginView,basename="auth")


urlpatterns = router.urls