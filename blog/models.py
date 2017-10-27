from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User') #Vinculo con otro modelo
	title = models.CharField(max_length=200) #Definimos un texto con N! limitado de caracteres
	text = models.TextField() #Textos sin un limite de caracteres
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self): #metodo publicar
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #Se obtiene un texto con un titulo
		return self.title