from django.urls import path, include
from delivery import views

urlpatterns = [
    path('order/', views.order_list, name="order_list"),

]
