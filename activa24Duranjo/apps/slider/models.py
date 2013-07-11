# coding: utf-8
from django.db import models


class SliderItem(models.Model):
	title = models.CharField(max_length=140)
	image = models.ImageField(upload_to='imgslider')

	def __unicode__(self):
		return self.title
