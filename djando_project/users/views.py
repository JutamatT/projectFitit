from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile,Review
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse

def home(request):
    Profiles = Profile.objects.order_by("-idShop").all()
    paginator = Paginator(Profiles, 3)
 
    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')
 
    try:
        # create Page object for the given page
        Profiles = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        Profiles = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        Profiles = paginator.page(paginator.num_pages)
    return render(request, 'users/home.html', {'Profiles': Profiles,
        'title' : 'MotorFixit'})


def myprofile(request):
    context = {
        'title' : 'MotorFixit'
        }
    return render(request, 'users/myprofile.html',context,)

def shop(request,idShop):
     return render(request, 'users/shop.html', {
        'id': Profile.objects.get(idShop=idShop),
        'scor': Review.objects.all(),
        'title' : 'MotorFixit'
    },)

def about(request):
    return render(request, 'users/about.html',{'title': 'About'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account has been created! you are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form,
        'title' : 'MotorFixit'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            p_form.save()
            u_form.save()
            messages.success(request, f'your account has been update!')
            return redirect('myprofile')
    else:
        u_form =UserUpdateForm(instance=request.user)
        p_form =ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'title' : 'MotorFixit'
    }
    return render(request, 'users/profile.html', context)
