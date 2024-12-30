from django.urls import path, include

urlpatterns = [
    path('api/products/', include('ecommerce.apps.products.urls')),
    path('api/orders/', include('ecommerce.apps.orders.urls')),
    path('api/users/', include('ecommerce.apps.users.urls')),
]