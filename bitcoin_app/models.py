from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.




class Portfolio(models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="images/")
    btc_total = models.DecimalField(max_digits=10, decimal_places=4,blank= True, null = True)
    eth_total = models.DecimalField(max_digits=10, decimal_places=4,blank= True, null = True)
    ltc_total = models.DecimalField(max_digits=10, decimal_places=4,blank= True, null = True)
    user_identifier = models.CharField(max_length=200, blank= True, null = True)

    def __str__(self):
        return self.user_identifier
    
    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    

class Transactions(models.Model):
    username = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, blank= True, null = True)
    id = models.AutoField(primary_key=True)
    transaction_ash = models.CharField(max_length=200, blank= True, null = True)
    transaction_date = models.DateField(default=timezone.now)
    currency = models.CharField(max_length=200, blank= True, null = True)
    amount = models.IntegerField(blank= True, null = True)

    

    def __str__(self):
        return self.transaction_ash
