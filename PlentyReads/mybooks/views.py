from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
# from .models import User
from django.utils import timezone
# from django.contrib.auth.forms import UserCreationForm

from mybooks.models import Book

from mybooks.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from mybooks.models  import User
from mybooks.models import *

from mybooks.forms import RegistrationForm, LoginForm
from mybooks import forms


from mybooks.models import Pdf, PdfManager, Html

from django.views.generic import ListView


def pdf(request):
    return render_to_response('showpdf/index.html', {})

def load_pdf(request):
    pdf=Pdf.fromUrl(request.GET["url_pdf"])
    pdf.save()
    return HttpResponseRedirect("/show/"+pdf.id)

def show_pdf(request, id_pdf):
    pdfSaved=Pdf.objects.get(id=id_pdf)
    html=None
    
    try:
        html=Html.objects.get(pdf=pdfSaved)
    except Html.DoesNotExist:
        html=Html(pdf=pdfSaved)
        pdfManager=PdfManager(pdfSaved);
        pdfManager.outToHtml(html)
        html.save()
    
    return HttpResponse(html.toString())
 
      # return HttpResponse(MEDIA_ROOT +pdfSaved.url)
     

# @csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            # user_form.save();
            # new_user = user_form.save(profile_callback=profile_callback)
            return HttpResponseRedirect('/register/success/')
    else:
        user_form = RegistrationForm()
    variables = RequestContext(request, {
    'form': user_form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

def login(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            email=user_form.cleaned_data['email']
            password=user_form.cleaned_data['password']
            user=User.objects.get(email=email)
            if(password!=user.password):
                return HttpResponseRedirect('.')
            else:
                return HttpResponseRedirect('/home/' + str(user.id))
    else:
        user_form = LoginForm()
    variables = RequestContext(request, {
    'form': user_form
    })
 
    return render(request, 'registration/login.html', {'form': user_form})


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# @login_required
def home(request, id_user):
    user=User.objects.get(id=id_user)
    logginUser = user.id
    # return render_to_response(
    # 'home.html',
    # { 'user': request.user }
    # )
    if logginUser is not None:
        return render(request, 'home.html');
        # +str(logginUser)
    else:
        return render(request, 'wrongLink.html');

class SearchView(generic.ListView):
  template_name = 'Search.html'
  context_object_name = 'latest_book_list'

  def get_queryset(self):
    """
    Return the last five published books (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
        create_date__lte=timezone.now()
    ).order_by('-create_date')[:5]

def search(request):
  return render_to_response('Search.html')


def profile(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST)
        if user_form.is_valid():
            password = user_form.cleaned_data['password']
            user = User.objects.get(id=8)
            user.password=password
            user.save()
            return HttpResponseRedirect('/profile/' )
    else:
        user_form = ProfileForm()
    variables = RequestContext(request, {
    'form': user_form
    })
    return render(request, 'registration/profile.html', {'form': user_form})



class KeySearchView(generic.ListView):
    template_name = 'Search.html'
    model = Book
    context_object_name = 'search_book_list'

    def get_queryset(self):
        try:
            name = self.request.GET.get('key') 
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter( bookname__icontains=name)
        else:
            object_list = self.model.objects.all()
        return object_list
def keysearch(request):
  return render_to_response('Search.html')

class LastestBooks_View(generic.ListView):
  # template_name = 'Search.html'
  context_object_name = 'latest_book_list'

  def get_queryset(self):
    """
    Return the last five published books (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
        create_date__lte=timezone.now()
    ).order_by('-create_date')[:5]

def latestBooks(request):
  return render_to_response('Search.html')

class bookView(generic.ListView):
  template_name = 'readbook.html'
  context_object_name = 'book_content_list'

  def get_queryset(self):
    """
    Return the last five published books (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
        create_date__lte=timezone.now()
    ).order_by('-create_date')[:5]

# def book(request):
#     pdf_data = open("/path/to/my/image.pdf", "rb").read()
#     return HttpResponse(pdf_data, mimetype="application/pdf")
def pdf_view(request):
    with open('/path/to/my/file.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed




# class F(FilterSet):
#     username = MethodFilter()
#     class Meta:
#         model = User
#         fields = ['username']

#     def filter_username(self, queryset, value):
#         return queryset.filter(
#             username__contains='ke'
#         )   