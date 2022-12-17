from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path(r'^/delete/user/(?P<pk>\d+)/$', views.delete_user, name="delete"),
    path('/edit/user/<str:pk>/', views.edit_user , name='edit')
    
]