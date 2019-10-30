from management import views
from django.urls import path

urlpatterns = [ 
    # url(r'^customers/$', views.customer_list),
    # url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail),

    path('customers/', views.get_customers, name="secure.customers"),
    path('customer/create/', views.create_employee, name="secure.customer.create"),

]
