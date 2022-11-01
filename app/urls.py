from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app import views
urlpatterns = [
    path('', views.HomePage,name="home"),
    path('anime',views.rendervideo,name="anime"),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path("register", views.register_request, name="register"),
    path("uploadvideo",views.showvideo,name="videoupload"),
    path('profile',views.userprofile,name='profile'),
    path('showvideo',views.showvideo,name="show_video")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)