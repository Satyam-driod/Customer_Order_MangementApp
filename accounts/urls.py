from django.urls import path
from . import views

app_name='accounts'
urlpatterns =[
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),

    path('account/',views.userProfile,name="profile"),
    path('user/',views.userPage,name='user-page'),

    path('',views.home,name="home"),
    path('products/',views.products,name="products"),
    path('orders/',views.orders,name="orders"),
    path('customer/<str:customer_id>/',views.customer,name="customer"),
    
    path('create_order/<str:customer_id>/',views.createOrder,name="create_order"),
    path('update_order/<str:order_id>/',views.updateOrder,name="update_order"),
    path('delete_order/<str:order_id>/',views.deleteOrder,name="delete_order"),
    path('Add_product/',views.AddProduct,name='Add_product'),

]