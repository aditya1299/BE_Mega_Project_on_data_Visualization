from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gsc-home'),
    path('about/', views.about, name='gsc-about'),
    path('signup/', views.signup, name='gsc-signup'),
    path('signin/', views.signin, name='gsc-signin'),
    path('addsite/', views.addsite, name='gsc-addsite'),
    path('documentation/', views.documentation, name='gsc-documentation'),
    path('letsstart/', views.letsstart, name='gsc-letsstart'),
    path('visualize/', views.visualize, name='gsc-visualize'),
    path('signup/register', views.register, name='gsc-register')

]
