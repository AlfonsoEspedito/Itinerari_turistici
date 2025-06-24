# Gestione Itinerari Turistici

Alfonso Espedito 0334000100

Web App sviluppata in Python Django per la gestione di itinerari turistici. Permette la registrazione e il login di utenti (turisti, guide, amministratori), la creazione di itinerari, la prenotazione da parte dei turisti e l’assegnazione delle guide. Il database è locale.

Alcune funzionalità potrebbero essere solo abbozzate a livello di template.

## Installazione
Per scaricare la repository eseguire il comando:
```
git clone https://github.com/AlfonsoEspedito/Itinerari_turistici.git
```
Una volta fatto ciò, entrare nella cartella `Itinerari` ed eseguire da terminale:
```
# Da powershell o cmd
python -m venv venv
```
E poi:
```
# Da PowerShell
venv/Scripts/activate
# Oppure
venv/Scripts/activate.ps1

# Da cmd
venv/Scripts/activate.bat
```
Ora che l'ambiente virtuale è attivo, è possibile installare le dipendenze con:
```
python -m pip install -r requirements.txt
```

## Utilizzo

Per avviare il server eseguire:
```
py manage.py runserver
```

Utenti di prova già registrati:
Turisti:
```
username: marcor
passw: marco
```
Guide:
```
username: peters
passw: peter
```
Amministratori:
```
username: giulia_neri
passw: giulia
```
