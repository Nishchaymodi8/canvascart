from django.urls import path
from .  import views 

urlpatterns=[
    path("",views.show_home,name="home"),   
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout_view,name="logout"),

]