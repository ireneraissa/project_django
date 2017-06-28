
from  django.db  import models
from django.urls import reverse


class Caracteristic(models.Model):
	name=models.TextField()
	surname=models.TextField()
	tel=models.IntegerField(default=0)
	def __str__(self):
		return self.name
		return self.surname 
		return self.tel

	def ajouter(self, char):
		#req=mixer.blend('bus_gestion.Caracteristic', name='francois')
		self.name= char
		return self.name
		# def deleting(self, var) :


	def get_absolute_url(self):
		return reverse('caracteristic-detail', args=[str(self.id)])

class Info(models.Model):
	#def information_bus(self):
	id_ecran=models.TextField()
	numero_matricule=models.IntegerField(default=0)
	numero_ligne=models.IntegerField(default=0)
	nombre_place=models.IntegerField(default=0)
	
	
	status_choice = (
		('O', 'opened'),
		('F', 'closed'),
	)
	status_ecran=models.CharField(max_length=1, choices=status_choice)
	chauffeur=models.ForeignKey(Caracteristic, on_delete=models.CASCADE)

	def __str__(self):
		return self.id_ecran

	def modify(self, element):
		self.numero_matricule=element
		return self.numero_matricule

	def get_absolute_url(self):
		return reverse('info-detail', args=[str(self.id)])

class Bus(models.Model):
	list_bus=models.ForeignKey(Info, on_delete=models.CASCADE)
	nom_bus=models.TextField()
	
	def __str__(self):
		return self.nom_bus
	
	def get_list_bus(self):	
		print(self.list_bus)
	def get_absolute_url(self):
		return reverse('bus-detail', args=[str(self.id)])