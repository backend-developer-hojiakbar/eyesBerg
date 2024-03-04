from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout_user, SignUpView
urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]