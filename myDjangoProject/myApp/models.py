from django.db import models

class PersonalDetails(models.Model):
	FullName  		= models.CharField(max_length = 120, null = True)
	DateOfBirth		= models.DateField(max_length = 120, null = True)
	Email			= models.CharField(max_length = 120, null = True)
	Phone		= models.CharField(max_length = 120, null = True)
	# OrganizerID		= models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',null = True)

	def __str__(self):
		return self.FullName
