from django.db import models
from apps.users.models import User
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True, null=True)
    wallet = models.DecimalField(default=0, decimal_places=4, max_digits=4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
    
    
