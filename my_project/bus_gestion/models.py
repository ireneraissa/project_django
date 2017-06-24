
from  django.db  import models


class Caracteristic(models.Model):
	name=models.TextField()
	surname=models.TextField()
	tel=models.IntegerField(default=0)
	def __str__(self):
		return self.name
		return self.surname 
		return self.tel

		#search_fields = ['name', 'surname', 'tel']
		# def nom(self):
		# 	self.name='irene raissa'
		# 	self.save()
		# def __str__(self):
		# 	return self.name, self.surname, self.tel

	def ajouter(self, char):
		#req=mixer.blend('bus_gestion.Caracteristic', name='francois')
		self.name= char
		return self.name
		# def deleting(self, var) :

	 # 		instance=self.filter
	 # 		delete(self.name==var)
	 # 		return self.name 


	 	#def Chauffeur(self):


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

class Bus(models.Model):
	list_bus=models.ForeignKey(Info, on_delete=models.CASCADE)
	nom_bus=models.TextField()
	
	def __str__(self):
		return self.nom_bus
	
	def get_list_bus(self):	
		print(self.list_bus)
