from src.app import app
from waitress import serve



if __name__ == '__main__': ## Si ce fichier est exécuté directement dans le terminal avec la commande "python wsgi.py"
    print("Lancement du serveur Waitress...")  
    serve(app, host='0.0.0.0', port=8080)  ## Lancer le serveur Waitress pour héberger l'application Flask sur toutes les interfaces réseau disponibles