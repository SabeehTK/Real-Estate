from django.urls import path
from accounts.views import Loginview,Registerview, Logoutview
from accounts.views import OtpVerificationView, LoginViaOtp

app_name = 'accounts'
urlpatterns = [
    path('login/', Loginview.as_view(), name='login'),
    path('loginviaotp/', LoginViaOtp.as_view(), name='loginviaotp'),
    path('otpverification/', OtpVerificationView.as_view(), name='otpverification'),
    path('register/', Registerview.as_view(), name='register'),
    path('logout/', Logoutview.as_view(), name='logout'),
]