from general.models import *
from general.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ManualSelectionView(APIView):

	def get(self, request):
		hosts = Host.objects.filter(pets=request.GET['pets'],
									family_structure=request.GET['family_structure'],
									allergies=request.GET['allergies'])
		serializer = HostSerializer(hosts, many=True)
		return Response(serializer.data)
