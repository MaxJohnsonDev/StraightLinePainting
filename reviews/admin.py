from django.contrib import admin
from .models import Review 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('name', 'comment', 'image', 'uploaded_at', 'status')
	list_filter = ('status', 'created', 'publish', 'name')
	search_fields = ('name', 'comment')
	