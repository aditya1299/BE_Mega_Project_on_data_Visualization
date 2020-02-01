from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='gsc-home'),
    path('about/', views.about, name='gsc-about'),
    path('signup/', views.signup, name='gsc-signup'),
    path('signin/', views.signin, name='gsc-signin'),
    path('signin/', views.addsite, name='gsc-addsite'),
    path('signin/', views.documentation, name='gsc-documentation'),
    path('signin/', views.letsstart, name='gsc-letsstart'),
    path('signin/', views.visualize, name='gsc-visualize'),

]

