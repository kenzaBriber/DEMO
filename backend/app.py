from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route pour afficher la page principale avec le formulaire
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Frontend avec Formulaire</title>
    </head>
    <body>
        <h1>Gestion d'un formulaire avec un bouton</h1>
        <form action="/click" method="POST">
            <button type="submit">Cliquez-moi</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(html)

# Route pour gérer la soumission du formulaire
@app.route('/click', methods=['POST'])
def handle_click():
    # Logique métier ici (par exemple, calcul ou traitement)
    result = "Bouton cliqué ! Logiciel traité dans le backend."

    # Retourner une page HTML comme réponse
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Résultat</title>
    </head>
    <body>
        <h1>Résultat</h1>
        <p>{result}</p>
        <a href="/">Retourner à l'accueil</a>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
