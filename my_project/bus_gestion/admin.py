from django.contrib import admin

# Register your models here.

from .models import Driver, Bus

class BusInline(admin.TabularInline):
    model = Bus
    extra = 1

class DriverAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Info Driver', {'fields': ['surname', 'name', 'tel']}),
    ]

	inlines=[BusInline]
	list_display = ('name', 'surname', 'tel')

admin.site.register(Driver, DriverAdmin)

