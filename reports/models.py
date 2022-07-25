from django.db import models
from accounts.models import User
from machines.models import Unit
from lookups.models import Ingredients, Cup


class ReportRefillIngredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    before = models.FloatField()
    after = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)


class ReportRefillCup(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)
    before = models.FloatField()
    after = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
