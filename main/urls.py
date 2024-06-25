
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/v1/auth/login/', TokenObtainPairView.as_view()),
    path('api/v1/auth/refresh-token/', TokenRefreshView.as_view()),
    
]
