from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from home_app.models import Profile
from .forms import UserForm,ProfileForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Create your views here.
def sinup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('app:all_boys')
    return render(request, 'accounts/sinup.html',{'form':form})
def profile(request):
    profile = Profile.object.get(user=request.user)
    return render(request,'profile.html',context={'profile':profile})


class RegisterPage(FormView):
    template_name = 'todo_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url= reverse_lazy('app:all_boys')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            auth_login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('app:all_boys')
        return super(RegisterPage,self).get(*args,**kwargs)


def edit_profile(request):
    profiles = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profiles)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            my_profile = profileform.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(reverse('app:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profiles)
    return render(request, 'accounts/edit_profile.html',{'user_form':userform,'profileform':profileform})