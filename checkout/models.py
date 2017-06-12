# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from products.models import MembershipProduct, EventProduct


class MembershipPayment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User)
	membership = models.ForeignKey(MembershipProduct)
	total = models.DecimalField(max_digits=6, decimal_places=2)


class EventPayment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(User)
	event = models.ForeignKey(EventProduct)
	total = models.DecimalField(max_digits=6, decimal_places=2)