from rest_framework import serializers

from .models import Planet,Character,People

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = People
        fields = [
            'id',
            'friends',
        ]


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = [
            'id',
            'name',
            'description',
            'code',
            'picture_url',
        ]
        
        
class CharacterSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Character
        fields = [
            'id',
            'name',
            'description',
            'picture_url',
            'planet',
            'people',
        ]