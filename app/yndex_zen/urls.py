
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views as acc_view



acc_router1 = DefaultRouter()
acc_router1.register('register', acc_view.AuthorRegisterAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include(acc_router1.urls)),
]
