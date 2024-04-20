from django.contrib import admin
from .models import CachedAPIRequest

@admin.register(CachedAPIRequest)
class CachedAPIRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'endpoint', 'request_data', 'created_at')
    list_display_links = ('user',)
    search_fields = ('user__username', 'endpoint', 'request_data')
    list_filter = ('created_at',)

    def has_add_permission(self, request):
        return False  

    def has_change_permission(self, request, obj=None):
        return False  
