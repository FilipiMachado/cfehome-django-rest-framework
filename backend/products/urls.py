from django.urls import path

from . import views

urlpatterns = [
   path('', views.product_list_create_view), # /api/products/
   path('<int:pk>/', views.product_detail_view),
]