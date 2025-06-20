from django.shortcuts import render, redirect, get_object_or_404
from .models import Turista, Guida, Amministratore, Itinerario, Prenotazione
from django.db import IntegrityError
import hashlib

def benvenuto(request):
    return render(request, 'benvenuto.html')

def registrazione(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        nazionalita = request.POST.get('nazionalita')

        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        if not all([nome, cognome, username, password, email, nazionalita]):
            return render(request, 'registrazione.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:

            turista = Turista(
                nome=nome,
                cognome=cognome,
                username=username,
                password=hashed_password,
                email=email,
                nazionalita=nazionalita
            )
            turista.save()


            return redirect('benvenuto')
        except IntegrityError:

            return render(request, 'registrazione.html', {'error_message': 'Username o email già in uso. Scegli un altro username o email.'})
        except Exception as e:

            return render(request, 'registrazione.html', {'error_message': f'Errore durante la registrazione: {str(e)}'})


    return render(request, 'registrazione.html')

def login_turista(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        if not all([username, password]):
            return render(request, 'login_turista.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:

            turista = Turista.objects.get(username=username)


            if turista.password == hashed_password:

                request.session['turista_username'] = turista.username
                request.session['turista_nome'] = turista.nome


                return redirect('principale')
            else:

                return render(request, 'login_turista.html', {'error_message': 'Username o password non validi.'})

        except Turista.DoesNotExist:

            return render(request, 'login_turista.html', {'error_message': 'Username o password non validi.'})
        except Exception as e:

            return render(request, 'login_turista.html', {'error_message': f'Errore durante il login: {str(e)}'})


    return render(request, 'login_turista.html')

def login_guida(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        if not all([username, password]):
            return render(request, 'login_guida.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:

            guida = Guida.objects.get(username=username)


            if guida.password == hashed_password:

                request.session['guida_username'] = guida.username
                request.session['guida_nome'] = guida.nome


                return redirect('principale_guida')
            else:

                return render(request, 'login_guida.html', {'error_message': 'Username o password non validi.'})

        except Guida.DoesNotExist:

            return render(request, 'login_guida.html', {'error_message': 'Username o password non validi.'})
        except Exception as e:

            return render(request, 'login_guida.html', {'error_message': f'Errore durante il login: {str(e)}'})


    return render(request, 'login_guida.html')

def login_amministratore(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        if not all([username, password]):
            return render(request, 'login_amministratore.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:

            amministratore = Amministratore.objects.get(username=username)


            if amministratore.password == hashed_password:

                request.session['amministratore_username'] = amministratore.username
                request.session['amministratore_nome'] = amministratore.nome


                return redirect('principale_amministratore')
            else:

                return render(request, 'login_amministratore.html', {'error_message': 'Username o password non validi.'})

        except Amministratore.DoesNotExist:

            return render(request, 'login_amministratore.html', {'error_message': 'Username o password non validi.'})
        except Exception as e:

            return render(request, 'login_amministratore.html', {'error_message': f'Errore durante il login: {str(e)}'})


    return render(request, 'login_amministratore.html')

def principale(request):

    if 'turista_username' not in request.session:

        return redirect('login_turista')


    username = request.session.get('turista_username')
    nome = request.session.get('turista_nome')


    itinerari = Itinerario.objects.filter(stato=True, maxpartecipanti__gt=0)


    return render(request, 'principale.html', {
        'username': username, 
        'nome': nome,
        'itinerari': itinerari
    })

def principale_guida(request):

    if 'guida_username' not in request.session:

        return redirect('login_guida')


    username = request.session.get('guida_username')
    nome = request.session.get('guida_nome')

    try:

        guida = Guida.objects.get(username=username)


        itinerari_assegnati = Itinerario.objects.filter(guida=guida)


        return render(request, 'principale_guida.html', {
            'username': username, 
            'nome': nome,
            'itinerari_assegnati': itinerari_assegnati
        })
    except Exception as e:

        print(f"Error: {e}")
        return render(request, 'principale_guida.html', {
            'username': username, 
            'nome': nome,
            'error_message': 'Si è verificato un errore nel recupero degli itinerari assegnati.'
        })

def prenota_itinerario(request):

    if 'turista_username' not in request.session:

        return redirect('login_turista')


    username = request.session.get('turista_username')

    if request.method == 'POST':

        itinerario_id = request.POST.get('itinerario_id')

        try:

            itinerario = Itinerario.objects.get(id_itinerario=itinerario_id)


            if itinerario.maxpartecipanti > 0:

                turista = Turista.objects.get(username=username)


                guida = Guida.objects.first()


                prenotazione = Prenotazione(
                    turista=turista,
                    itinerario=itinerario,
                    guida=guida
                )
                prenotazione.save()


                itinerario.maxpartecipanti -= 1
                itinerario.save()


                return redirect('itinerari_prenotati')
            else:

                return redirect('principale')
        except Exception as e:

            print(f"Error: {e}")
            return redirect('principale')


    return redirect('principale')

def itinerari_prenotati(request):

    if 'turista_username' not in request.session:

        return redirect('login_turista')


    username = request.session.get('turista_username')
    nome = request.session.get('turista_nome')

    try:

        turista = Turista.objects.get(username=username)


        prenotazioni = Prenotazione.objects.filter(turista=turista)


        return render(request, 'itinerari_prenotati.html', {
            'username': username, 
            'nome': nome,
            'prenotazioni': prenotazioni
        })
    except Exception as e:

        return redirect('principale')

def rimuovi_prenotazione(request, prenotazione_id):

    if 'turista_username' not in request.session:

        return redirect('login_turista')


    username = request.session.get('turista_username')

    try:

        turista = Turista.objects.get(username=username)


        prenotazione = get_object_or_404(Prenotazione, Id_prenotazione=prenotazione_id, turista=turista)


        itinerario = prenotazione.itinerario


        itinerario.maxpartecipanti += 1
        itinerario.save()


        prenotazione.delete()


        return redirect('itinerari_prenotati')
    except Exception as e:

        print(f"Error: {e}")
        return redirect('itinerari_prenotati')

def principale_amministratore(request):

    if 'amministratore_username' not in request.session:

        return redirect('login_amministratore')


    username = request.session.get('amministratore_username')
    nome = request.session.get('amministratore_nome')


    guide = Guida.objects.all()


    if request.method == 'POST':

        titolo = request.POST.get('titolo')
        descrizione = request.POST.get('descrizione')
        durata = request.POST.get('durata')
        maxpartecipanti = request.POST.get('maxpartecipanti')
        tema = request.POST.get('tema')
        guida_username = request.POST.get('guida')


        if not all([titolo, descrizione, durata, maxpartecipanti, tema, guida_username]):
            return render(request, 'principale_amministratore.html', {
                'username': username, 
                'nome': nome,
                'guide': guide,
                'error_message': 'Tutti i campi sono obbligatori.'
            })

        try:

            guida = Guida.objects.get(username=guida_username)


            itinerario = Itinerario(
                titolo=titolo,
                descrizione=descrizione,
                durata=durata,
                maxpartecipanti=int(maxpartecipanti),
                tema=tema,
                stato=True,
                guida=guida
            )
            itinerario.save()


            return render(request, 'principale_amministratore.html', {
                'username': username, 
                'nome': nome,
                'guide': guide,
                'success_message': f'Itinerario "{titolo}" creato con successo e assegnato a {guida.nome} {guida.cognome}.'
            })

        except Exception as e:

            return render(request, 'principale_amministratore.html', {
                'username': username, 
                'nome': nome,
                'guide': guide,
                'error_message': f'Errore durante la creazione dell\'itinerario: {str(e)}'
            })


    return render(request, 'principale_amministratore.html', {
        'username': username, 
        'nome': nome,
        'guide': guide
    })
