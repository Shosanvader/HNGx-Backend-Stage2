from rest_framework import serializers
from .models import Person
from . import validators

#serializes data according to the Person model, adding a layer of validation and security 
class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [validators.validate_unique_name])
    class Meta:
        model = Person
        fields= [
            'id',
            'name'
        ]
