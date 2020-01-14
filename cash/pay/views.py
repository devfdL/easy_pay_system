from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from .forms import dataqr
import imutils
import re
import time
import csv
from transactions.models import payment


def index(request):
    data_box = dataqr()
    context ={
      'judul':'',
      'content':'Wellcome to my web.',
      'webname': 'Cash',
      'data_box': data_box,
    }

    if request.method == 'POST':
      #print(request.POST['data'])
      data_qr = request.POST['data']
      inputStr = data_qr
      m = re.search('.*:(.*),(.*)->', inputStr)
      print ("toko = " + m.group(1))
      print ("harga = " + m.group(2))
      price = int(m.group(2))
      place = m.group(1)
      #get last data
      path = './Data/'
      lis = list(csv.reader(open(path + request.user.username + '.csv')))
      #get last list
      some_list = lis[-1]
      #get last balance
      lastmoney = int(some_list[-1])

      xmoney = lastmoney -price

      uname = request.user.username

      #update new data
      f_path = './Data/'
      f = open(f_path + uname +'.csv', "a")
      f.write('\n')
      f.write(time.strftime('%d/%b/%Y') + ',' + str(xmoney))
      f.close()

      payment.objects.create(
          sender = uname,
          place = place,
          nominal = str(price),
          date = time.strftime('%d/%b/%Y'),
      )

    return render(request, 'pay/index.html', context)