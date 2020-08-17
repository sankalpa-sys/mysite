
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('aboutme/',include('aboutme.urls')),
    path('signup/',include('signup.urls')),
    path('login/',include('login.urls')),
    path('logout/',include('logout.urls')),
    path('prof/',include('prof.urls')),
    path('contact/',include('contact.urls'))
]
