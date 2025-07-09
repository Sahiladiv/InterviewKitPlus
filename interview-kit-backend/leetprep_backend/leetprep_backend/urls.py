from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # All API endpoints
    path('api/problems/', include('problems.urls')),
    path('api/auth/', include('authapp.urls')),
    path('api/submissions/', include('submission.urls')),
    path('api/mock/', include('mockinterview.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/explanation/', include('explanation.urls')),  
]
