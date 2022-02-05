from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.

class telegramsControl(models.Model):
	priority_ = [('1', 'Висока'), ('0', 'Низька')]
	date = models.CharField(max_length=200,blank=True,verbose_name='Дата виконання:')
	unit_to_report = models.CharField(max_length=100, null=True, verbose_name='Кому доповісти:')
	tlg_number = models.CharField(max_length=100, null=True, verbose_name='Номер вихідної телеграми')
	description = models.TextField(verbose_name= 'Опис телеграми')
	priority = models.CharField(max_length=20, choices=priority_,  verbose_name='Важливість телеграми', default=0)
	tlg_scan = models.FileField(upload_to='tlg_storage', null=True, blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                                verbose_name='Завантажити скан-копію телеграми')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True)
	confirm = models.BooleanField(default=False, verbose_name='Телеграма виконана!')

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('index')
