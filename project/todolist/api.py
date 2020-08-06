from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


#get all jobs

@api_view(['GET'])
def job_list_api(request):
	all_jobs=Post.objects.all()
	data=PostSerializer(all_jobs,many=True).data
	return Response({'data':data})

#get one job

@api_view(['GET'])
def job_detail(request,id):

	job_detaill=Post.objects.get(id=id)
	data=PostSerializer(job_detaill).data
	return Response({'data':data})

	#class basid voews
class PostList(generics.ListAPIView):
	model=Post
	queryset= Post.objects.all()
	serializer_class = PostSerializer
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PostSerializer
	queryset=Post.objects.all()
	lookup_field='id'







