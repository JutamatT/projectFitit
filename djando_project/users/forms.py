from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Review



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='อีเมล')
    first_name =forms.CharField(label='ชื่อ')
    last_name =forms.CharField(label='นามสกุล')

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='อีเมล')
    first_name =forms.CharField(label='ชื่อ')
    last_name =forms.CharField(label='นามสกุล')

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name' ]

class ProfileUpdateForm(forms.ModelForm):
    nameShop =forms.CharField(label='ชื่อร้าน')
    description =forms.CharField(label='รายละเอียด',widget=forms.Textarea(attrs={"rows":5, "cols":25}))
    dateTimeOpen =forms.CharField(label='เวลาเปิดทำการ')
    dateTimeClose =forms.CharField(label='เวลาปิดทำการ')
    phone1 =forms.CharField(label='หมายเลขโทร')
    phone2 =forms.CharField(label='หมายเลขโทร')
    image =forms.ImageField(label='รูปภาพ')
    le = forms.DecimalField(widget= forms.TextInput
                           (attrs={'class':'some_class',
				   'id':'le'}))
    lo = forms.DecimalField(widget= forms.TextInput
                           (attrs={'class':'some_class',
				   'id':'lo'}))

    class Meta:
        model = Profile
        fields = ['nameShop','description','dateTimeOpen','dateTimeClose','phone1','phone2', 'image','le','lo']
        