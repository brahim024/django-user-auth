from django.db import models

# Create your models here.
class Map:
  location= models.CharField(max_length=20)
  destination= models.CharField(max_length=20)
  destance=models.DecimalField(max_digits=10,decimal_places=2)
  created=models.DateTimeField(auto_now=True)
  def __str__(self):
    return f"im destinate from {self.location} to {self.destination} is {self.destance}"