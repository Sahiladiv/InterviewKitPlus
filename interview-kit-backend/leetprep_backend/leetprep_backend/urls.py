from django.contrib import admin
from django.urls import path, include


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # All API endpoints
    path('api/problems/', include('problems.urls')),
    path('api/auth/', include('authapp.urls')),
    path('api/submissions/', include('submission.urls')),
    path('api/mock/', include('mockinterview.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/explanation/', include('explanation.urls')),  
]
