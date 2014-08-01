from general.models import *
from general.serializers import *
from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class HostList(generics.ListCreateAPIView):
	queryset = Host.objects.all()
	serializer_class = HostSerializer

class HostDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Host.objects.all()
	serializer_class = HostSerializer

class AllergieList(generics.ListCreateAPIView):
	queryset = Allergie.objects.all()
	serializer_class = AllergieSerializer

class AllergieDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Allergie.objects.all()
	serializer_class = AllergieSerializer

class PetList(generics.ListCreateAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetSerializer

class PetDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetSerializer

class FamilyStructureList(generics.ListCreateAPIView):
	queryset = FamilyStructure.objects.all()
	serializer_class = FamilyStructureSerializer

class FamilyStructureDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = FamilyStructure.objects.all()
	serializer_class = FamilyStructureSerializer

class FamilyStructurePreferenceList(generics.ListCreateAPIView):
	queryset = FamilyStructurePreference.objects.all()
	serializer_class = FamilyStructurePreferenceSerializer

class FamilyStructurePreferenceDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = FamilyStructurePreference.objects.all()
	serializer_class = FamilyStructurePreferenceSerializer

class RequestList(generics.ListCreateAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer

class RequestDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer