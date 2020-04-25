from django.urls import path
from first_app import views

urlpatterns=[
    path('table',views.table,name='table'),
    path('test',views.test,name='test'),
    path('index',views.index,name='index'),
    path('form',views.form_name_view,name="form_name"),
    path('users',views.user_view,name="user_name"),
    path('adduser',views.add_user,name="add_user")
]
