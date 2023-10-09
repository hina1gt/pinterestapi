from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', customuser),
    path('user/<int:pk>/', customuser_detail),
    path('post/', post),
    path('post/<int:pk>/', post_detail),
    path('categoty/', category),
    path('categoty/<int:pk>/', category_detail),

    path('auth/', include('dj_rest_auth.urls')),
]