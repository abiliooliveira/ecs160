from django.forms import widgets
from rest_framework import serializers
from general.models import *

class FamilyStructureSerializer(serializers.ModelSerializer):
	class Meta:
		model = FamilyStructure
		fields = ('id', 'description')

class FamilyStructurePreferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = FamilyStructurePreference
		fields = ('id', 'student', 'structure','preference')

class AllergieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Allergie
		fields = ('id', 'name')

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = (	'id', 'name', 'email', 'username', 'password', 
        			'phone_number', 'address', 'mailing_address',
        			'short_blurb', 'allergies',)

class HostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Host
		fields = (	'id', 'name', 'email', 'username', 'password', 
        			'phone_number', 'address', 'mailing_address',
        			'short_blurb', 'pets', 'allergies', 'family_structure')

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pet
		fields = ('id', 'animal')

class RequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields = ('id', 'student', 'host', 'status', 'created', 'last_modified', 'hangout_date')