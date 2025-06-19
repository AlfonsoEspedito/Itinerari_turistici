from django.shortcuts import render, redirect
from .models import Turista
from django.db import IntegrityError
import hashlib

# Create your views here.
def benvenuto(request):
    return render(request, 'benvenuto.html')

def registrazione(request):
    if request.method == 'POST':
        # Get form data
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        nazionalita = request.POST.get('nazionalita')

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Validate data
        if not all([nome, cognome, username, password, email, nazionalita]):
            return render(request, 'registrazione.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:
            # Create new Turista object
            turista = Turista(
                nome=nome,
                cognome=cognome,
                username=username,
                password=hashed_password,
                email=email,
                nazionalita=nazionalita
            )
            turista.save()

            # Redirect to benvenuto page on success
            return redirect('benvenuto')
        except IntegrityError:
            # Handle case where username or email already exists
            return render(request, 'registrazione.html', {'error_message': 'Username o email già in uso. Scegli un altro username o email.'})
        except Exception as e:
            # Handle other errors
            return render(request, 'registrazione.html', {'error_message': f'Errore durante la registrazione: {str(e)}'})

    # If GET request, just render the form
    return render(request, 'registrazione.html')

def login_turista(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Validate data
        if not all([username, password]):
            return render(request, 'login_turista.html', {'error_message': 'Tutti i campi sono obbligatori.'})

        try:
            # Try to find the turista with the given username
            turista = Turista.objects.get(username=username)

            # Check if the password matches
            if turista.password == hashed_password:
                # Store user info in session
                request.session['turista_username'] = turista.username
                request.session['turista_nome'] = turista.nome

                # Redirect to principale page on success
                return redirect('principale')
            else:
                # Password doesn't match
                return render(request, 'login_turista.html', {'error_message': 'Username o password non validi.'})

        except Turista.DoesNotExist:
            # Turista with the given username doesn't exist
            return render(request, 'login_turista.html', {'error_message': 'Username o password non validi.'})
        except Exception as e:
            # Handle other errors
            return render(request, 'login_turista.html', {'error_message': f'Errore durante il login: {str(e)}'})

    # If GET request, just render the form
    return render(request, 'login_turista.html')

def login_guida(request):
    return render(request, 'login_guida.html')

def login_amministratore(request):
    return render(request, 'login_amministratore.html')

def principale(request):
    # Check if user is logged in
    if 'turista_username' not in request.session:
        # If not logged in, redirect to login page
        return redirect('login_turista')

    # Get user info from session
    username = request.session.get('turista_username')
    nome = request.session.get('turista_nome')

    # Render the principale template with user info
    return render(request, 'principale.html', {'username': username, 'nome': nome})
