from django.shortcuts import render
import qrcode
from PIL import Image
from qr_code.qrcode.utils import ContactDetail
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
import time
import subprocess
import csv
from transactions.models import payment


# Create your views here.
from .forms import bill
from .models import payment

def index(request):
    bill_box = bill()
   
    posts = payment.objects.filter().order_by('-id')
    #result = reversed(list(posts))
    context ={
      'judul':'Transactions',
	    'webname': 'Cash',
      'bill_box': bill_box,
      'posts': posts,
    }

    if request.method == 'POST':
      global tprice
      global data
      tprice = request.POST['price']
      #print(tprice)
      
    
      # The data that you want to store
      data = "123:"+ request.user.username +", "+ tprice+"->"
      context['data'] = data

      template = loader.get_template("transactions/pay.html")
      context = {'data': data, 'tprice':tprice}
      return HttpResponse(template.render(context, request))

    
    return render(request,'transactions/index.html', context)

def send_command(request):
    bill_box = bill()
    posts = payment.objects.filter().order_by('-id')
    subprocess.Popen(["python3","face-recog.py"], close_fds=False)

    time.sleep(9)
    path = './payment/'
    lis = list(csv.reader(open(path + 'pay-data.csv')))
    #get last list
    pay_by = lis[-1]
    #get last balance
    print(pay_by[-1])

    uname = pay_by[-1]

    if uname == 'unknown':
      template = loader.get_template("transactions/pay.html")
      context = {'data': data, 'tprice':tprice, 'err_msg': 'Unknown face id!'}
      return HttpResponse(template.render(context, request))
    else:
      #get last data
      path = './Data/'
      lis = list(csv.reader(open(path + pay_by[-1] +'.csv')))
      #get last list
      some_list = lis[-1]
      #get last balance
      lastmoney = int(some_list[-1])

      xmoney = lastmoney - int(tprice)

      print(xmoney)
      #update new data
      f_path = './Data/'
      f = open(f_path + uname +'.csv', "a")
      f.write('\n')
      f.write(time.strftime('%d/%b/%Y') + ',' + str(xmoney))
      f.close()

      output = 'payment was successfully (ID: '+ pay_by[-1] +')'
      template = loader.get_template("transactions/sucsess.html")
      context = {'output': output}

      payment.objects.create(
          sender = uname,
          place = request.user.username,
          nominal = tprice,
          date = time.strftime('%d/%b/%Y'),
      )

    time.sleep(10)

    return HttpResponse(template.render(context, request))