from rest_framework import serializers
from .models import PersonalDetails

class personaldetailsserializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalDetails

		fields = '__all__'