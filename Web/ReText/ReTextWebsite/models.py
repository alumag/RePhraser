from __future__ import unicode_literals

from django.db import models

class Sentence(models.Model):
	Sentence_text = models.CharField(max_length=2048)

# Create your models here.
