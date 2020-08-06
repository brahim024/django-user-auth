from django.urls import path,include
from .import views
from .import api
app_name='todolist'
urlpatterns = [
    path('', views.all_post,name='all_post'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.post, name='job_details'),
    # api
    path('api/list', api.job_list_api, name='job_list_api'),
    path('api/list/<int:id>',api.job_detail , name='job_detail'),

     # class basid url
    path('api/v2/jobs', api.PostList.as_view(), name='job_list_api'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='job_detail_api'),
    

    ]
