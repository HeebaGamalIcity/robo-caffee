from rest_framework import serializers
from reports.models import ReportRefill


class ReportRefillIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportRefill
        fields = '__all__'