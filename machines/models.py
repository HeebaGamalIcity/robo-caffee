from django.db import models


class Unit(models.Model):
    ar_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    serial_number = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='unit/', null=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.en_name}"


class Machine(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.IntegerField(unique=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Timer(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.IntegerField(unique=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    value = models.PositiveIntegerField(default=0)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Sensor(models.Model):
    Reading_TYPE_CHOICES = [
        ('int', 'Integer'),
        ('float', 'Float'),
        ('bool', 'Bool'),
        ('str', 'string'),
    ]
    name = models.CharField(max_length=100)
    serial_number = models.IntegerField(unique=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    reading_type = models.CharField(max_length=6, choices=Reading_TYPE_CHOICES)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class ReadingSensor(models.Model):
    value = models.CharField(max_length=6)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
