from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/<str:target>/plus/', views.plus, name='plus'),
    path('<int:user_pk>/<str:target>/minus/', views.minus, name='minus'),
    path('<int:user_pk>/<str:target>/reset/', views.reset, name='reset'),
]


