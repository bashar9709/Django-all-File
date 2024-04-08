from django.urls import path
from first_app.views import home, signup, user_login, profile, user_logout, pass_change, pass_change2

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup , name="signup"),
    path('login/', user_login, name="login"),
    path('logout/',user_logout, name="logout"),
    path('profile/', profile, name="profile"),
    path('pass_change/', pass_change, name="passchange"),
    path('pass_change2/', pass_change2, name="passchange2"),
]