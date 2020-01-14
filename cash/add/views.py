from django.shortcuts import render
import time

# Create your views here.
from .forms import Bankacc
from .models import addCustomer
import csv

def index(request):
    acc_box = Bankacc()
   
    context ={
      'judul':'add',
	    'webname': 'Cash',
      'acc_box': acc_box,
    }

    if request.method == 'POST':
      #print(request.POST)
      fname = request.POST['f_name']
      lname = request.POST['l_name']
      bd = request.POST['birthday']
      allmoney = request.POST['allmoney']
      uname = request.POST['u_name']
      f_path = './Data/'
      f = open(f_path + uname +'.csv', "a")
      f.write('\n')
      f.write(time.strftime('%d/%b/%Y') + ',' +allmoney)
      f.close()

      addCustomer.objects.create(
          u_name = uname,
          f_name = fname,
          l_name = lname,
          birthday = bd,
      )
      
    
    return render(request,'add/index.html', context)


def add_fund(request):
  acc_box = Bankacc()
  
  context ={
    'judul':'add',
    'webname': 'Cash',
    'acc_box': acc_box,
  }

  if request.method == 'POST':
    #print(request.POST)
    allmoney = request.POST['allmoney']
    uname = request.POST['u_name']

    path = './Data/'
    lis = list(csv.reader(open(path + uname +'.csv')))
    #get last list
    some_list = lis[-1]
    #get last balance
    lastmoney = int(some_list[-1])

    xmoney = lastmoney + int(allmoney)

    print(xmoney)
    #update new data
    f_path = './Data/'
    f = open(f_path + uname +'.csv', "a")
    f.write('\n')
    f.write(time.strftime('%d/%b/%Y') + ',' + str(xmoney))
    f.close()
    
  
  return render(request,'add/add.html', context)