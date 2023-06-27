
# from django.contrib import admin
# from django.urls import path
# from myapp import views
# from django.conf import settings
# from django.conf.urls.static import static

# # from resumeuploader.myapp.views import Conform_password

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',views.HomeView.as_view(), name='home'),
#     path('<int:pk>',views.CandidateView.as_view(), name='candidate'),
#     path('',views.SignupPage,name='signup'),
#     path('login/',views.LoginPage,name='login'),
#     path('logout/',views.LogoutPage,name='logout'),
#     # path('forget/',views.ForgetPage,name='forget'),
#     # path('conform_password/',views.Conform_password,name='Conform_password')
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('forget/', views.ForgetPage, name='forget'),
    path('conform_password/', views.ConformPasswordPage, name='conform_password'),
    path('conform_password/<str:token>/', views.ConformPasswordPage, name='conform_password_with_token'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
