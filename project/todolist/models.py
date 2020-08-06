from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify #import slugify
#create coices of job types
JOB_TYPE= [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
]
#image uploade
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
    #oportinitisw jobs
class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=20)
    job_type= models.CharField(max_length=20,choices=JOB_TYPE)
    desciptions= models.TextField(max_length=1000)
    pub_date= models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    city= models.CharField(max_length=20)
    contry= models.CharField(max_length=20)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image= models.ImageField(upload_to=image_upload)
    slug= models.SlugField(blank=True,null=True)
    #creat slug in page
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,** kwargs)
    def __str__(self):
        return self.title
    #create Category
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    #apply for any jobs
class Apply(models.Model):
    job=models.ForeignKey(Post,related_name='apply_job',on_delete=models.CASCADE)
    your_name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Website=models.URLField()
    Upload_CV=models.FileField(upload_to='apply/')
    Coverletter=models.TextField(max_length=600)
    pub_dat= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.your_name
       

