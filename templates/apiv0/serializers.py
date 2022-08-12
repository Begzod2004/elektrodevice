from rest_framework import serializers
from technique.models import *


class TechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technique
        fields = '__all__'



class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        


class AksiyaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aksiya
        fields = '__all__'
