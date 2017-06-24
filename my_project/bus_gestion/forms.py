from django import forms

from .models import  Caracteristic, Info 


class CaracteristicForm(forms.ModelForm):
	class Meta:
		model=Caracteristic

		fields=('name', 'surname', 'tel' )

	def clean_name_surname_tel(self):
		data=self.cleaned_data.get('name', 'surname', 'tel') ##  It take the  the place whwere we have name surname  and  tel, after that if you want to introduice someting in that place look at the test_forms 
		#data2=self.cleaned_data.get('surname')
		#data3=self.cleaned_data.get('tel')
		if len(data.name) >= 10:
			raise forms.ValidationError('are you sure it is your name?')
		return data


class ChoiceInline(forms.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

	inlines=[ChoiceInline]
	list_display = ('question_text', 'pub_date')
		
	#def modifier(self, data):
		#req=self.get('name')
			#if req != data:
			#	raise forms.ValidationError('i change the name')
			#return data