from django.db import models

# Create your models here.
class RouterDetails(models.Model):
	rid=models.AutoField(primary_key=True)
	sapid=models.CharField(max_length=18,unique=True)
	hostname=models.CharField(max_length=14,unique=True)
	loopbackid=models.CharField(max_length=150)
	mac_add=models.CharField(max_length=100,unique=True)
	def __str__(self):
		return self.sapid