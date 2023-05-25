from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

def onas(request):
    return render(request, 'onas.html')

def glowna(request):
    return render(request, 'glowna.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    lekarze = Lekarz.objects.all()
    pensjonariusze = Pensjonariusz.objects.all()
    recepty = Recepty.objects.all()
    d = 0
    p = 0
    a = 0

    for i in lekarze:
        d+=1
    for i in pensjonariusze:
        p+=1
    for i in recepty:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}

    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('admin_login')

def Podglad_pracownika(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Lekarz.objects.all()
    d = {'doc': doc}
    return render(request, 'podglad_pracownika.html', d)

def Usun_pracownika(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    lekarz = Lekarz.objects.get(id = pid)
    lekarz.delete()
    return redirect('podglad_pracownika')


def Dodaj_pracownika(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n = request.POST['imie']
        na = request.POST['nazwisko']
        m = request.POST['dane_kontaktowe']
        sp = request.POST['specjalizacja']
        try:
            Lekarz.objects.create(imie=n, nazwisko=na, dane_kontaktowe=m, specjalizacja=sp)
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}
    return render(request, 'dodaj_pracownika.html', d)

def Podglad_pensjonariusza(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Pensjonariusz.objects.all()
    d = {'doc': doc}
    return render(request, 'podglad_pensjonariusza.html', d)

def Usun_pensjonariusza(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    pensjonariusz = Pensjonariusz.objects.get(id = pid)
    pensjonariusz.delete()
    return redirect('podglad_pensjonariusza')

def Dodaj_pensjonariusza(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n = request.POST['imie']
        na = request.POST['nazwisko']
        d = request.POST['data_urodzenia']
        p = request.POST['plec']
        da = request.POST['dane_kontaktowe']
        inf = request.POST['informacje_medyczne']
        #h = request.POST['historia_leczenia']

        try:
            Pensjonariusz.objects.create(imie=n, nazwisko=na, data_urodzenia=d, plec=p, dane_kontaktowe=da, informacje_medyczne=inf)
            error = 'no'
        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'dodaj_pensjonariusza.html', d)


def Dodanie_recepty(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    lekarze = Lekarz.objects.all()
    pensjonariusze = Pensjonariusz.objects.all()

    if request.method == "POST":
        lekarz_id = request.POST['lekarz']
        pensjonariusz_id = request.POST['pensjonariusz']
        data_wystawienia = request.POST['datawys']
        zalecone_leki = request.POST['leki']

        try:
            lekarz = Lekarz.objects.get(id=lekarz_id)
            pensjonariusz = Pensjonariusz.objects.get(id=pensjonariusz_id)
            Recepty.objects.create(lekarz=lekarz, pensjonariusz=pensjonariusz, data_wystawienia=data_wystawienia,
                                   zalecone_leki=zalecone_leki)
            error = 'no'
        except Exception as e:
            print(e)  # Wyświetlenie informacji o błędzie w konsoli
            error = 'yes'

    d = {'error': error, 'lekarze': lekarze, 'pensjonariusze': pensjonariusze}
    return render(request, 'dodanie_recepty.html', d)


def Widok_recept(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Recepty.objects.all()
    d = {'doc': doc}
    return render(request, 'widok_recept.html', d)

def Usun_recepte(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    recepty = Recepty.objects.get(id = pid)
    recepty.delete()
    return redirect('widok_recept')



