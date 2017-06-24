from django.contrib import admin

# Register your models here.

from .models import Caracteristic, Info

class InfoInline(admin.TabularInline):
    model = Info
    extra = 2

class CaracteristicAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['surname']}),
        (None,                {'fields':['tel']}),
    ]

	inlines=[InfoInline]
	list_display = ('name', 'surname', 'tel')

admin.site.register(Caracteristic, CaracteristicAdmin)

