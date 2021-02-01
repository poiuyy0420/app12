from django.urls import path
from apis.views import UserCreateView, UserLoginView

urlpatterns = [
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user_create'),
    path('vi/users/login/', UserLoginView.as_view(), name='apis_v1_user_login')
]
