from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views
from firstapp.views import StoreViewSet, UserStoreViewSet, AdminStoreViewSet

stores_router = DefaultRouter()
stores_router.register(r'stores', StoreViewSet)

my_stores_router = SimpleRouter()
my_stores_router.register(r'my_stores', UserStoreViewSet, basename='my_stores')

admin_stores_router = SimpleRouter()
admin_stores_router.register(r'admin_stores', AdminStoreViewSet)

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('today/', views.today, name='today'),
    path('my_name/', views.my_name, name='my_name'),
    path('calculator/', views.calculator, name='calculator'),
    path('stores_apiview/', views.StoreList.as_view()),
]

urlpatterns += stores_router.urls
urlpatterns += my_stores_router.urls
urlpatterns += admin_stores_router.urls
