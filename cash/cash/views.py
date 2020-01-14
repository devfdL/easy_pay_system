import datetime
from django.utils.timezone import utc
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import csv
from transactions.models import payment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreationForm



# Create your views here.

def index(request):
    #posts = payment.objects.filter().order_by('-id')[:1]
    posts = payment.objects.filter().order_by('-id')[:1]
    result = reversed(list(posts))
    #print(result)
    context ={
      'judul':'Home',
      'content':'Wellcome to my web.',
      'webname': 'Cash',
      'posts': posts,
    }

    if request.user.is_authenticated:
       if request.user.username != 'admin1' and request.user.first_name != 'toko':
         path = './Data/'
         lis = list(csv.reader(open(path + request.user.username + '.csv')))
         #get last list
         some_list = lis[-1]
         #get last balance
         context['balance'] = some_list[-1]


    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm

    context={
        'form': form,
    }

    
    return render(request, "main/register.html", context)