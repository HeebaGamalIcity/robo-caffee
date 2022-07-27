from rest_framework import serializers
from reports.models import ReportRefillCup, ReportRefillIngredient


class ReportRefillCupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportRefillCup
        fields = '__all__'


class ReportRefillIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportRefillIngredient
        fields = '__all__'