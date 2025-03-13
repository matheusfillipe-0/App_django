from django.urls import path
from promotions.views import detail_promotion 
from promotions.views import login_view

urlpatterns = [
    path('<int:promotion_id>/', detail_promotion, name='detail_promotion'),
    path('login/', login_view, name='login'),
]