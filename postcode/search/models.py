from django.db import models

class src_postcode(models.Model):
	names = models.CharField(max_length = 7)
	postcode = models.CharField(max_length = 7)
