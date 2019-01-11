from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import PersonalDetails

import requests
import json
import urllib

import json
from django.core import serializers



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import personaldetailsserializer

class index(View):
	def get(self, request, *args, **kwargs):
		return render(request,'myApp/index.html')

class detailslist(APIView):
	def get(self,request):
		pdetails = PersonalDetails.objects.all()
		serializer = personaldetailsserializer(pdetails,many=True)

		# inventory_detail = serializers.serialize('json', invetoryRecord.objects.all())
		# inventory_data = [d['fields'] for d in json.loads(inventory_detail)]
		
		return Response(serializer.data)
		# return render(request,'myApp/dataAPI.html')

	def post(self,request,*args,**kwargs):
		
		# print('Frontend Data')
		# data = self.request.data
		# print(data.get('name'))
		# print(request.data)
		# print('Post Request Accepted')

		PersonalDetails.objects.create(
			FullName 	= self.request.data.get('name'),
			DateOfBirth	= self.request.data.get('age'),
			Email		= self.request.data.get('address'),
			Phone		= self.request.data.get('department'),
			)

		return JsonResponse({'message' : 'Data - Received'})



