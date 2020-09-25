from django.urls import path
from . import views
app_name='markdown'
urlpatterns=[
	path('login/',views.user_login,name='login'),

]