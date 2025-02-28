from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clothes/', views.clothes, name='clothes'),
    path('jeans/', views.jeans, name='jeans'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("logout/", views.logout, name="logout"),
    path('shoes/', views.shoes, name='shoes'),
    path('accessories/', views.accessories, name='accessories'),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('profile/', views.profile, name="profile"),
	path('order/', views.order, name="order"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)