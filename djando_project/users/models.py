from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idShop =models.AutoField(primary_key=True)
    nameShop = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dateTimeOpen = models.TimeField(auto_now=False,blank=True, null=True)
    dateTimeClose = models.TimeField(auto_now=False,blank=True, null=True)
    phone1 = models.CharField(max_length=10,blank=True, null=True)
    phone2 = models.CharField(max_length=10,blank=True, null=True)
    le = models.DecimalField(max_digits=20,decimal_places=15,blank=True, null=True)
    lo = models.DecimalField(max_digits=20,decimal_places=15,blank=True, null=True)
    image = models.ImageField(default='profile.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username}Profile'

    def save(self, *arge, **kawrgs):
        super().save(*arge, **kawrgs)

class UserP(models.Model):
    userP = models.CharField(max_length=200,blank=False, null=False)
    passp = models.CharField(max_length=200,blank=False, null=False)

class Review(models.Model):
    scor = models.DecimalField(max_digits=1,decimal_places=1,blank=True, null=True)
    idShop = models.OneToOneField(Profile, on_delete=models.CASCADE,blank=True, null=True)
    idScor =models.AutoField(primary_key=True)
    userP = models.OneToOneField(UserP,on_delete=models.CASCADE,blank=True, null=True)



    

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width >300 :
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

