from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth import login
from django.contrib import messages #import messages
import re

from django.conf import settings
from django.contrib.auth.decorators import login_required


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"

# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"



def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        username = form.cleaned_data.get('username')
        return redirect('login')
    else:
      form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

#The first checks to see if the form is being posted while 
#the second checks to see if the form is valid. 
#If both are true, then the form information is saved under a user,
# the user is logged in, and the user is redirected to the homepage 
#showing a success message.

#Else, if the form is not valid, an error message is shown. 
#But if the request is not a POST in the first place, 
#meaning the first if statement returned false, 
#render the empty form in the register template. 
@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   #request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
  
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
  
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
  
    return render(request, 'users/profileupdate.html', context)