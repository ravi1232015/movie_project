from django.db import models

# Create your models here.
class user(models.Model):
	Movie_name=models.CharField(max_length=30)
	User_name=models.CharField(max_length=30)
	Email=models.EmailField()
	Phone=models.IntegerField()
	No_of_seat=models.IntegerField()
	Date=models.DateField()
	
	# cho=(('PVR','PVR'),('INOX','INOX'),)
	# theater=(models.ChoiceField(cho=cho))
	# 	