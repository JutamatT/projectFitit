from rest_framework import serializers
from users.models import Profile,Review,UserP
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','idShop','nameShop','description','dateTimeOpen','dateTimeClose','phone1','phone2', 'image','le','lo']

class ReviewSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Review
        fields = ['scor','idScor','idShop','userP']

class UserPSerializer(serializers.ModelSerializer):        
    class Meta:
        model = UserP
        fields = ['userP','passp']
        