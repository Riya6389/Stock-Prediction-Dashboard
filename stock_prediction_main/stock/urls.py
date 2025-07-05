from django.urls import path
from .views import predictions_list
from .views import (
    dashboard,
    RegisterView,
    register_page,
    login_page,
    logout_page,
    predict_stock,
    health_check,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # 🔹 Dashboard (Protected Page)
    path('', dashboard, name='dashboard'),

    # 🔹 Register & Login/Logout (HTML Pages)
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    # 🔹 REST API: User Registration
    path('api/v1/register/', RegisterView.as_view(), name='register'),

    # 🔹 REST API: JWT Token Endpoints
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔹 REST API: Stock Prediction (protected by JWT)
    path('api/v1/predict/', predict_stock, name='predict_stock'),   # ✅ Correct REST path

    # 🔹 Health Check (for Docker CI/CD)
    path('healthz/', health_check, name='health_check'),
    path('api/v1/predictions/', predictions_list, name='predictions_list'),

]
