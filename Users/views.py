from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView
from .forms import RegisterForm, ProfileUpdate
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile



User = get_user_model()
def activate_user_view(request, code=None, *args, **kwargs):
    print(User)
    pass
    if code:
        qs = User.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
               user_ = profile
               user_.is_active = True
               user_.save()
               profile.activated = True
               profile.activation_key = None
               profile.save()
               print("YOU ARE SO VERY WELCOME ")
               return redirect("/accounts/login")
    return redirect("/accounts/login")



class RegisterView(CreateView):
	form_class = RegisterForm
	template_name ='registration/register.html' 
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		# if self.request.user.is_authenticated:
		#  	return redirect('/logout')
		return super(RegisterView, self).dispatch(*args, **kwargs)



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Users/update_profile.html'
    form_class = ProfileUpdate
    login_url = '/login/'

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
