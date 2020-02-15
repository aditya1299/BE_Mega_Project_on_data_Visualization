from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gsc-home'),
    path('about/', views.about, name='gsc-about'),
    path('signup/', views.signup, name='gsc-signup'),
    path('logout/', views.logout, name='gsc-logout'),
    path(r'signin/', views.signin, name='gsc-signin'),
    path('addsite/', views.addsite, name='gsc-addsite'),
    path('viewsites/', views.viewsites, name='gsc-viewsites'),
    path('documentation/', views.documentation, name='gsc-documentation'),
    path('viewsites/letsstart', views.letsstart, name='gsc-letsstart'),
    path('viewsites/letsstart/visualize/', views.visualize, name='gsc-visualize'),
    path('signup/register', views.register, name='gsc-register'),
    path('signin/signin_action', views.signin_action, name='gsc-signin_action'),
    path('addsite/addsite_action', views.addsite_action, name='gsc-addsite_action'),
    path('graph', views.graph, name='gsc-graph'),
    path('viewsites/authorize',views.authorize,name='gsc-authorization'),
    path('oauth2callback', views.handleOAuth2Callback, name='gsc-oauth-handler')
]
