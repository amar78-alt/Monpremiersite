# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Routes ajoutées pendant les exercices
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Amar", nom="Alle")


@app.get("/loisirs")
def loisirs():
    return "J'aime le sport, l'informatique et découvrir de nouvelles choses."


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{a} + {b} = {a + b}"


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")

    return f"Bonjour {prenom}, qui vient de {ville} ! (reçu en {request.method})"


# Exercice 9 : redirection et codes de statut
@app.get("/home")
def home():
    return redirect("/")


@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


# Exercice 10 : en-têtes envoyés par le navigateur
@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
