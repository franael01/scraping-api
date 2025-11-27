from flask import Flask , request,jsonify
from src.services.scraping_test import scraping_test

app = Flask(__name__)


@app.route('/sakura/test')
def sakura_test():
    
    return "First solo API !"

@app.route('/sakura/post_test', methods=['POST'])
def sakura_post_test():
    data = request.get_json()
    # Affiche le type et le contenu
    print("Type de data:", type(data))
    print("Contenu de data:", data)

    # Affiche ce que jsonify crée
    response = jsonify(data)
    print("Type de response:", type(response))
    print("Response object:", response)
    print("Response data (bytes):", response.data)
    print("Response data (décodé):", response.data.decode('utf-8'))
    char = data['test'].replace(' ', '_').upper()
    print(type(char), type(jsonify(char)))
    return jsonify(char), 200

@app.route('/sakura/scraping_test', methods=['POST'])
def sakura_app_test():
    data = request.get_json()
    url = data['url']
    result = scraping_test(url)
    return jsonify(result), 200