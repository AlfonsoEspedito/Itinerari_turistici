from django.db import models

class Lingua(models.Model):

    nome = models.CharField(max_length=100, primary_key=True)


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

class Itinerario(models.Model):

    Id_itinerario = models.CharField(primary_key=True)
    titolo = models.CharField(max_length=100, null=True)
    descrizione = models.CharField(max_length=100, null=True)
    durata = models.CharField(max_length=100, null=True)
    maxpartecipanti = models.IntegerField()
    tema = models.CharField(max_length=100, null=True)
    stato = models.BooleanField()


class Feedback(models.Model):

    Id_feedback = models.IntegerField(primary_key=True)
    valutazione = models.IntegerField()
    commento = models.CharField(max_length=100, null=True)
    data = models.DateField(null=True)
    turista = models.ForeignKey(Turista, on_delete=models.CASCADE)

class Visita(models.Model):

    Id_visita = models.IntegerField(primary_key=True)
    data = models.DateField()
    oraInizio = models.DateField()
    oraFine = models.DateField()
    puntoIncontro = models.CharField(max_length=100, null=True)
    guida = models.ForeignKey(Guida, on_delete=models.CASCADE)
    stato = models.BooleanField()
    numpersone = models.IntegerField()
    descrizione = models.CharField(max_length=100, null=True)


class Prenotazione(models.Model):

    Id_prenotazione = models.IntegerField(primary_key=True)
    turista = models.ForeignKey(Turista, on_delete=models.CASCADE)
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE)