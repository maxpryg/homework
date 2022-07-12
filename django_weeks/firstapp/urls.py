from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views
from firstapp.views import StoreViewSet, UserStoreViewSet, AdminStoreViewSet

router = DefaultRouter()
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'my_stores', UserStoreViewSet, basename='my_stores')
router.register(r'admin_stores', AdminStoreViewSet, basename='admin_stores')

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('today/', views.today, name='today'),
    path('my_name/', views.my_name, name='my_name'),
    path('calculator/', views.calculator, name='calculator'),
    path('stores_apiview/', views.StoreList.as_view()),
]

urlpatterns += router.urls
