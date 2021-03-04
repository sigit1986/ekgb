from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import (
    authenticate,
    login,
    logout)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import csv, io
from .models import *
import urllib, json
from django.contrib.auth.decorators import login_required

# Create your views here.

alamat = 'http://202.179.184.151/'

def LoginView(request):
    form = UserLoginForm(request.POST or None)
    template_name = 'pegawai/detail.html'
    data = {
            'form': form,
            'judul': 'Dashboard',
        }
    if not form.is_valid():
        return render(request, "login/login.html")
    else :
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        request.session['username'] = username
        login(request, user)
        return render(request, template_name, context= {'data':data, 'user':user})

def LogoutView(request):
    try:
        logout(request)
        del request.session['username']
    except KeyError:
        pass
    return render(request, 'login/login.html')


def IndexView(request):
    alamat = 'http://202.179.184.151/'
    username = str(request.session.get('username'))
    pegawai = {
        'title': "Data Pegawai",
        'subtitle' : username,
    }
    datautama =  urllib.request.urlopen(alamat +'nip/?search='+username)
    json_str = json.load(datautama)
    print (json_str)
    return render(request, 'pegawai/index.html', context = {'json_str':json_str, 'pegawai':pegawai})

def UploadView(request):
    # deklarasi Template
    template = "pegawai/uploaduser.html"
    data = User.objects.all()
    pegawai = PegawaiModel.objects.all()
    akun = AkunModel.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Table Head berupa username, email, password',
        'profiles': data,
        'pegawai':pegawai,
        'akun':akun    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = User.objects.get_or_create(
            id = column[0],
            username=column[1],
            email=column[2],
            password=make_password(column[3]))
        # Akuns = AkunModel.objects.create(
        #     jenis_akun=column[9],
        #     akun = column[4],
        #     pegawai = column[0])
        context = {}
    return render(request, template, context)

def PegawaiUploadView(request):
    # deklarasi Template
    template = "pegawai/pegawaiupload.html"
    pegawai = PegawaiModel.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Table Head berupa username, email, password',
        'pegawai':pegawai,
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = PegawaiModel.objects.get_or_create(
            id = column[0],
            nama = column[1],
            nip = column[2],
            opd = column[3],
            pengguna = column[4],
            telpon = column[5],
            pangkat = column[6]
            )
        context = {}
    return render(request, template, context)

def LogoutView(request):
    try:
        logout(request)
        del request.session['username']
    except KeyError:
        pass
    return render(request, 'login/login.html')


def IndexView(request):
    username = str(request.session.get('username'))
    pegawai = {
        'title': "Data Pegawai",
        'subtitle' : username,
    }
    datautama =  urllib.request.urlopen(alamat +'nip/?search='+username)
    json_str = json.load(datautama)
    print (json_str)
    return render(request, 'pegawai/index.html', context = {'json_str':json_str, 'pegawai':pegawai})

@login_required 
def PegawaiUploadView(request):
    # deklarasi Template
    template = "pegawai/uploadpegawai.html"
    data = User.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Table Head berupa username, email, password',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = User.objects.update_or_create(
            username=column[0],
            email=column[1],
            password=make_password(column[2])
        )
        context = {}
    return render(request, template, context)


@login_required
def DetailView(request):
    username = str(request.session.get('username'))
    pegawai = User.objects.get(username=username)
    print(pegawai)
    datautama =  urllib.request.urlopen(alamat +'nip/?company='+'937')
    json_str = json.load(datautama)
    print(json_str)
    return render(request, 'pegawai/detail.html',context={'json_str':json_str})

