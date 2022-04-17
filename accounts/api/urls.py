from django.urls import path
from django import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django import views
from .views import registration_view,trainer_registration

urlpatterns = [ 
    path('trainer_registraion/',trainer_registration,name='trainer_registration'),

    path('trainer_login/',TokenObtainPairView.as_view(),name='tokenobtainpair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='tokenrefresh'),

    path('register/',registration_view,name='register'),
    
    path('login',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]