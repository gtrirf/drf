from rest_framework import serializers
from .models import CategorySigns, RoadSigns  # Corrected import for RoadSigns

class CategorySignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySigns
        fields = '__all__'

class RoadSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSigns
        fields = '__all__'
