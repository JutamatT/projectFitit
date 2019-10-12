from rest_framework.viewsets import ModelViewSet
from users.models import Profile,Review,UserP
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer,ReviewSerializer,UserPSerializer
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserPViewSet(ModelViewSet):
    queryset = UserP.objects.all()
    serializer_class = UserPSerializer