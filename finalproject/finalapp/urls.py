


from django.urls import path
from . import views
urlpatterns = [

    path('',views.demo,name='demo'),
    path('home', views.home, name='home'),
    path('register',views.register,name='register'),
    path('logout', views.logout, name='logout'),
    path('login',views.login,name='login'),
    # path('detail', views.detail, name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('add',views.add_movi,name='add_movi'),
    path('detail/<int:movie_id>/', views.detail,name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    # path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]