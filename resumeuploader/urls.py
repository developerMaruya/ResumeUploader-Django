
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HomeView.as_view(), name='home'),
    path('<int:pk>',views.CandidateView.as_view(), name='candidate'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('home/',views.Home,name='home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
