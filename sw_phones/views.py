from django.shortcuts import render
from sw_phones.models import Telefones
import re

def index(request):
    phones = Telefones.objects.order_by('switch_up_to')
    context = {'phones': phones}
    return render(request,'sw_phones/phones.html',context)


def phones(request):
    phones = Telefones.objects.order_by('switch_up_to')
    context = {'phones': phones}
    return render(request,'sw_phones/phones.html',context)

def getArpPhones():
    phones = Telefones.objects.order_by('setor')
    return aphList


