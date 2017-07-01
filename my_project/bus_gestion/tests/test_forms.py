from .. import forms
from ..models import Driver, Bus

import pytest
class TestDriverform:
	def test_forms(self):

		form= forms.DriverForm(data={})
		
		assert form.is_valid() is False, 'Should valid if no data given'

		form=forms.DriverForm(data={'name':'kameni', 'surname':'irene', 'tel' : 771710292})

		assert form.is_valid() is True, 'should be '

		assert frozenset({'name', 'surname', 'tel'}) not in form.errors, 'should hae body field errors'
	#def test_modifier(self):
		#form = forms.CaracteristicForm(req={'name' : 'aims'},)

		#assert form.is_valid is False, 'should be said if the form have change' 