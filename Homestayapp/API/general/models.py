from django.db import models

REQUEST_STATUS = (
	('1','Processing'),
	('2','Authorized'),
	('3','Accepted'),
)

class Pet(models.Model):
	animal = models.CharField(max_length=100, blank=False)

class Allergie(models.Model):
	name = models.CharField(max_length=100, blank=False)

class FamilyStructure(models.Model):
	description = models.TextField(max_length=100, blank=False)

class Host(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.CharField(max_length=100, blank=False)
	username = models.CharField(max_length=100, blank=False)
	password = models.CharField(max_length=100, blank=False)
	phone_number = models.CharField(max_length=100, blank=False)
	address = models.CharField(max_length=100, blank=False)
	mailing_address = models.CharField(max_length=100, blank=False)
	short_blurb = models.TextField(max_length=100, blank=False)
	pets = models.ManyToManyField(Pet)
	allergies = models.ManyToManyField(Allergie)
	family_structure = models.ForeignKey(FamilyStructure)

class Student(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.CharField(max_length=100, blank=False)
	username = models.CharField(max_length=100, blank=False)
	password = models.CharField(max_length=100, blank=False)
	phone_number = models.CharField(max_length=100, blank=False)
	address = models.CharField(max_length=100, blank=False)
	mailing_address = models.CharField(max_length=100, blank=False)
	short_blurb = models.TextField(max_length=100, blank=False)
	allergies = models.ManyToManyField(Allergie)
	# family_structure_preferences = models.ManyToManyField(FamilyStructure, through='FamilyStructurePreference', related_name='fsp',)
	# pet_preferences = models.ManyToManyField(Pet, through='PetPreference', related_name='pp')

class FamilyStructurePreference(models.Model):
	student = models.ForeignKey(Student,)
	structure = models.ForeignKey(FamilyStructure,)
	preference = models.IntegerField(default=0)

class PetPreference(models.Model):
	student = models.ForeignKey(Student,)
	pet = models.ForeignKey(Pet,)
	preference = models.IntegerField(default=0)

class PublicProfileInformation(models.Model):
	student = models.ForeignKey(Student, unique=True)
	name = models.BooleanField(default=True)
	email = models.BooleanField(default=True)
	username = models.BooleanField(default=True)
	password = models.BooleanField(default=True)
	phone_number = models.BooleanField(default=True)
	address = models.BooleanField(default=True)
	mailing_address = models.BooleanField(default=True)
	short_blurb = models.BooleanField(default=True)
	pet_preference = models.BooleanField(default=True)
	allergies = models.BooleanField(default=True)
	family_structure_preference = models.BooleanField(default=True)

class Request(models.Model):
	student = models.ForeignKey(Student)
	host = models.ForeignKey(Host)
	status = models.CharField(choices=REQUEST_STATUS, max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now_add=True)
	hangout_date = models.DateTimeField(blank=True)



























