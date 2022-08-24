from django.db import models

class Configuration(models.Model):
	value_token = models.FloatField(default = 0.1)
	value_token_transaction = models.TextField(null=True,blank=True)

