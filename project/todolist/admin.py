from django.contrib import admin

# Register your models here.
from .models import Post , Category , Apply
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Apply)
#Post is a model class
