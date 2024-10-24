import operator
from calendar import monthrange
from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db import connection
from django.db.models.signals import post_save, pre_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils import timezone
from django.utils.safestring import mark_safe


class PageVisit(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	visits = models.PositiveIntegerField(default=0)

	class Meta:
		verbose_name = 'Счетчик'
		verbose_name_plural = 'Счетчики'