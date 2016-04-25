from django.contrib import admin

# Register your models here.
from .models import resource

class ResourceAdmin(admin.ModelAdmin):
	list_display = ["title","updated", "timestamp"]
	list_display_links = ["updated", "title"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "description"]
	class Meta:
		model = resource
	
		
admin.site.register(resource, ResourceAdmin)