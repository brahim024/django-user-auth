from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		#giv hem job models name
		model=Post
		#giv hem my models field 
		fields='__all__'


