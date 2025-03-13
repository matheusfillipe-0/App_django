from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from promotions.views import detail_promotion
from promotions.views import login_view


urlpatterns = [
    path('', home_view),
    path('promotions/', include('promotions.urls')),
    path('login/', login_view, name='login'),  
    path('admin/', admin.site.urls),
 
]
