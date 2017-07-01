from  django.db  import models
from django.urls import reverse


class Driver(models.Model):
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
		return reverse('info-detail', args=[str(self.id)])


class Bus(models.Model):	
	nom_bus=models.TextField()
	id_ecran=models.TextField()
	numero_matricule=models.IntegerField(default=0)
	numero_ligne=models.IntegerField(default=0)
	nombre_place=models.IntegerField(default=0)
	
	
	status_choice = (
		('O', 'opened'),
		('F', 'closed'),
	)
	status_ecran=models.CharField(max_length=1, choices=status_choice)
	chauffeur=models.ForeignKey(Driver, on_delete=models.CASCADE)


	def modify(self, element):
		self.numero_matricule=element
		return self.numero_matricule
	
	def __str__(self):
		return self.nom_bus

	def get_absolute_url(self):
		return reverse('bus-detail', args=[str(self.id)])