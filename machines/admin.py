from django.contrib import admin
from .models import Unit, Machine, Timer, Sensor, ReadingSensor
# Register your models here.


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number")


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "unit")


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "unit", "machine")


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "machine", "value")


@admin.register(ReadingSensor)
class ReadingSensorAdmin(admin.ModelAdmin):
    list_display = ("sensor", "value", "updated_at")
