import pytest
from mixer.backend.django import mixer
import pandas  as pd
pytestmark = pytest.mark.django_db

class TestBus:
 	def test_model(self):
 		obj=mixer.blend('bus_gestion.Bus')

 		assert obj.pk == 1, 'Should create Bus in instance'

# xdg-open htmlcov/index.html to see the coverage
 	
 	#def test_modification(self):
 	#	obj=mixer.blend('bus_gestion.Bus',)
class TestCaracteristic:

	def test_Chauffeur(self):
		obj=mixer.blend('bus_gestion.Caracteristic', name='last name', surname='first name', tel=771710292)
		assert obj.name == 'last name'
		assert obj.surname == 'first name'
		assert obj.tel ==  771710292
	def test_ajouter(self):
 		obj=mixer.blend('bus_gestion.Caracteristic')
 		resp=obj.ajouter('francois')

 		assert 'francois' in obj.name, 'should add a new name of the driver'
	def test_delete(self) :

 		obj=mixer.blend('bus_gestion.Caracteristic', mame='last name')
 		req=obj.delete()
 		assert 'last name' not in obj.name, 'should add a new name of the driver'

	#def test_import_csv(self):
 	#	obj=mixer.blend('bus_gestion.Caracteristic', name='raissa')
 	#	resp=pd.DataFrame({'irene':obj.name, index})
 	#	resp.to_csv('infos.csv', index=False)
 	#	req=pd.read_csv(info.csv)
#		 def __str__(self):
#		assert req is csv_file




class Test_Info:
 	def test_information_bus(self):
 		obj=mixer.blend('bus_gestion.Info', numero_matricule=35478, numero_ligne=3, nombre_place=60, id_ecran='23-ff-58-90', status_ecran='O')

 		result=obj.status_ecran

 		assert obj.numero_matricule==35478
 		assert obj.numero_ligne==3
 		assert obj.nombre_place==60
 		assert obj.id_ecran=='23-ff-58-90'
 		assert result != 'F'

 	def test_modify(self):

 		obj=mixer.blend('bus_gestion.Info', numero_matricule=35478)
 		result=obj.modify(12345)
 		
 		assert result == 12345, 'should change the value of matricule'