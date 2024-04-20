from django.db import models
from accounts.models import Account

class CachedAPIRequest(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    endpoint = models.CharField(max_length=100)
    request_data = models.TextField()
    response_data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.endpoint}"
