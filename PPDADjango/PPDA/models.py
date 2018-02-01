from __future__ import unicode_literals

from django.db import models

# Create your models here.

class dataUpload(models.Model):
	docFile = models.FileField(upload_to = 'documentUpload/%Y/%m/%d')
	epsilon = models.FloatField(null = True, blank = True, default = None) 
	sensitivity = models.FloatField(null = True, blank = True, default = None) 