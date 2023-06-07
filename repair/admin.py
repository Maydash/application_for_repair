from django.contrib import admin
from .models import ApplicationForPrinter

# admin.site.register(ApplicationForPrinter)

@admin.register(ApplicationForPrinter)
class ApplicationForPrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cabinet', 'phone_number', 'created_at', 'status')
    list_display_links = ('name', 'cabinet',)
    search_fields = ('cabinet', 'phone_number', 'created_at', 'status')
    list_filter = ('status',)
    ordering = ('id','cabinet','created_at', 'status')
