from django.urls import path
# 导入simplejwt默认内置视图，因为本来就写好了，直接引入urls即可
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('profile/', UserProfileView.as_view())
] 