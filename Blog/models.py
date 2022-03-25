from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL
class Blogs(models.Model):
	user            = models.ForeignKey(User, on_delete=models.CASCADE)
	title           = models.CharField(max_length=120)
	content         = models.TextField(help_text="separate each item by a comma")


	def get_absolute_url(self):
		return reverse("Blog:Blog_list")

	def __str__(self):
		return self.title.capitalize()



class Likes(models.Model):
	post       = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	status     = models.CharField(max_length=120)
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})

	def __str__(self):
		return self.post.title.capitalize()



class Comments(models.Model):
	post            = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	content         = models.TextField(help_text="separate each item by a comma")
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})	
	def __str__(self):
		return self.post.title.capitalize()

