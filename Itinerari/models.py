from django.db import models
from django.utils import timezone

class Lingua(models.Model):

    nome = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nome


class Amministratore(models.Model):

    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True,unique=True)
    ente = models.CharField(max_length=100,null=True)

class Turista(models.Model):

    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True,unique=True)
    nazionalita = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class Tappa(models.Model):

    ID_tappa=models.CharField(primary_key=True)
    nome = models.CharField(max_length=100, null=True)
    descrizione = models.CharField(max_length=100, null=True)
    luogo = models.CharField(max_length=100, null=True)


class Guida(models.Model):

    nome = models.CharField(max_length=100, null=True)
    cognome = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    abilitazione = models.CharField(max_length=100,null=True)
    lingua = models.ForeignKey(Lingua, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Itinerario(models.Model):

    id_itinerario = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=100, null=True)
    descrizione = models.CharField(max_length=100, null=True)
    durata = models.CharField(max_length=100, null=True)
    maxpartecipanti = models.IntegerField()
    tema = models.CharField(max_length=100, null=True)
    stato = models.BooleanField()
    guida = models.ForeignKey(Guida, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titolo



class Prenotazione(models.Model):

    Id_prenotazione = models.AutoField(primary_key=True)
    turista = models.ForeignKey(Turista, on_delete=models.CASCADE)
    itinerario = models.ForeignKey(Itinerario, on_delete=models.CASCADE, null=True)
    data_prenotazione = models.DateTimeField(default=timezone.now)
