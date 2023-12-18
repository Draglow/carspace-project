from django.urls import path
from . import views
urlpatterns = [
   path('',views.cars,name='cars'),
   path('<int:id>',views.detail_car,name='detail_car'),
   path('search',views.search,name='search')
]
