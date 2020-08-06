from django import forms
from .models import Apply
from .models import Post

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['your_name','Email','Website','Upload_CV','Coverletter']
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=('user','slug')
