from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from .models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from mybooks.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'mybooks/index.html'
    context_object_name = 'latest_User_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.order_by('-create_date')[:5]

class HomeView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_User_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.order_by('-create_date')[:5]

def index(request):
    # latest_User_list = User.objects.order_by('-create_date')[:5]
    # context = {'latest_User_list': latest_User_list}
    return render_to_response('index.html')
