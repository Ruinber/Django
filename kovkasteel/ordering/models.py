from django.db import models

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=30, verbose_name='Имя')
	phone = models.CharField(max_length=30, verbose_name='Телефон')
	email = models.EmailField(verbose_name='Email', blank=True)
	message = models.TextField(max_length=3000,verbose_name='Описание проекта')
	photo = models.ImageField(verbose_name='Фото', blank=True, default=None, upload_to='media/%Y-%m-%d/')


	def __str__(self):
		return self.name

	class Mete:
		verbose_name = 'Клинты'
		verbose_name_plural = 'Клинты'
		ordering = ['name', 'photo']