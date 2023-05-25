from django.urls import path
from .views import onas, glowna, kontakt, Login, Logout_admin, Index, Podglad_pracownika, Usun_pracownika
from .views import Dodaj_pracownika, Podglad_pensjonariusza, Usun_pensjonariusza,  Dodaj_pensjonariusza
from .views import Widok_recept, Usun_recepte, Dodanie_recepty

urlpatterns = [
    path('', glowna, name='glowna'),
    path('onas/', onas, name='onas'),
    path('kontakt/', kontakt, name='kontakt'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),

    path('podglad_pracownika/', Podglad_pracownika, name='podglad_pracownika'),
    path('usun_pracownika(?P<int:pid>)/', Usun_pracownika, name='usun_pracownika'),
    path('dodaj_pracownika/', Dodaj_pracownika, name='dodaj_pracownika'),

    path('podglad_pensjonariusza/', Podglad_pensjonariusza, name='podglad_pensjonariusza'),
    path('usun_pensjonariusza(?P<int:pid>)/', Usun_pensjonariusza, name='usun_pensjonariusza'),
    path('dodaj_pensjonariusza/', Dodaj_pensjonariusza, name='dodaj_pensjonariusza'),

    path('widok_recept/', Widok_recept, name='widok_recept'),
    path('usun_recepte(?P<int:pid>)/', Usun_recepte, name='usun_recepte'),
    path('dodanie_recepty/', Dodanie_recepty, name='dodanie_recepty'),

]